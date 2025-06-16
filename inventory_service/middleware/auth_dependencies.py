from typing import Optional
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from inventory_service.models.auth import TokenData, User
from inventory_service.utils.auth_utils import verify_password, get_password_hash
from inventory_service.config.auth_settings import auth_settings
import hmac
import hashlib
import base64
import json
import time
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
security = HTTPBearer()

# Single user stored in memory (loaded from .env)
def get_admin_user() -> User:
    """Get the single admin user from environment variables"""
    return User(
        username=auth_settings.ADMIN_USERNAME,
        email=auth_settings.ADMIN_EMAIL,
        full_name=auth_settings.ADMIN_FULL_NAME,
        is_admin=True
    )

def get_admin_hashed_password() -> str:
    """Get the hashed password for the admin user"""
    # You might want to cache this to avoid hashing on every request
    return get_password_hash(auth_settings.ADMIN_PASSWORD)

def authenticate_user(username: str, password: str) -> Optional[User]:
    """Authenticate against the single admin user"""
    admin_user = get_admin_user()
    
    # Check if username matches
    if username != admin_user.username:
        return None
    
    # Check password (compare with plain text from .env)
    # Note: In production, you'd want to store the hashed password in .env
    if password != auth_settings.ADMIN_PASSWORD:
        return None
    
    return admin_user

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token = credentials.credentials
        payload = jwt.decode(token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    # Verify the username matches our admin user
    admin_user = get_admin_user()
    if token_data.username != admin_user.username:
        raise credentials_exception
    
    return admin_user

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    # Since we only have one user, and they're admin, no additional checks needed
    return current_user

async def get_current_user_from_cookie(request: Request) -> User:
    """NEW: Cookie-based dependency - reads JWT from cookie"""
    
    jwt_token = request.cookies.get("access_token")
    
    if not jwt_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authentication cookie found. Please login using /auth/login-cookie",
        )
    
    try:
        payload = jwt.decode(jwt_token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(401, "Invalid token payload")
    except JWTError:
        raise HTTPException(401, "Invalid authentication token. Please login again.")
    
    admin_user = get_admin_user()
    if username != admin_user.username:
        raise HTTPException(401, "Invalid user")
    
    return admin_user

async def get_current_user_from_cookie_production(request: Request) -> User:
    
    # Extract JWT token from cookie
    jwt_token = request.cookies.get("access_token")
    
    if not jwt_token:
        logger.warning(f"Authentication attempt without cookie from IP: {request.client.host}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authentication cookie found. Please login using /auth/login-cookie",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Validate JWT format before processing
    try:
        parts = jwt_token.split('.')
        if len(parts) != 3:
            logger.warning(f"Invalid JWT format from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token format",
            )
        
        header_encoded, payload_encoded, signature_encoded = parts
        
    except Exception as e:
        logger.warning(f"JWT parsing error from IP: {request.client.host} - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token structure",
        )
    
    #VERIFY SIGNATURE FIRST (CRITICAL SECURITY STEP)
    try:
        # Recreate the signed message
        message = f"{header_encoded}.{payload_encoded}"
        
        # Calculate expected signature using our secret key
        expected_signature_raw = hmac.new(
            auth_settings.SECRET_KEY.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).digest()
        
        # Encode expected signature same way as received signature
        expected_signature_encoded = base64.urlsafe_b64encode(
            expected_signature_raw
        ).decode('utf-8').rstrip('=')
        
        # Use constant-time comparison to prevent timing attacks
        signature_valid = hmac.compare_digest(signature_encoded, expected_signature_encoded)
        
        if not signature_valid:
            logger.warning(f"Invalid JWT signature from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token signature - token has been tampered with",
            )
        
        logger.debug("JWT signature verification successful")
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Signature verification error from IP: {request.client.host} - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token signature verification failed",
        )
    
    # Only NOW is it safe to decode and trust the payload
    try:
        # Decode payload (safe now that signature is verified)
        def base64url_decode(data):
            padding = 4 - len(data) % 4
            if padding != 4:
                data += '=' * padding
            return json.loads(base64.urlsafe_b64decode(data).decode('utf-8'))
        
        # Decode and validate header
        header = base64url_decode(header_encoded)
        if header.get('alg') != auth_settings.ALGORITHM:
            logger.warning(f"Unsupported algorithm {header.get('alg')} from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Unsupported algorithm: {header.get('alg')}",
            )
        
        # Decode payload (now safe since signature is verified)
        payload = base64url_decode(payload_encoded)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Token decoding error from IP: {request.client.host} - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token encoding",
        )
    
    # Step 5: Comprehensive time-based validations
    try:
        current_time = int(time.time())
        
        # Check expiration (exp claim)
        exp_time = payload.get('exp')
        if not exp_time:
            logger.warning(f"Token missing expiration from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing expiration time",
            )
        
        if current_time >= exp_time:
            exp_datetime = datetime.fromtimestamp(exp_time)
            logger.info(f"Expired token from IP: {request.client.host}, expired at: {exp_datetime}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired. Please login again.",
            )
        
        # Check issued-at time (iat claim) - prevent tokens from future
        iat_time = payload.get('iat')
        if iat_time and current_time < iat_time:
            logger.warning(f"Token from future from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token used before valid time",
            )
        
        # Check not-before time (nbf claim) if present
        nbf_time = payload.get('nbf')
        if nbf_time and current_time < nbf_time:
            logger.warning(f"Token used before nbf time from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token not yet valid",
            )
        
        # Optional: Check maximum token age (additional security)
        if iat_time and (current_time - iat_time) > (24 * 3600):  # 24 hours max
            logger.warning(f"Token too old from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token too old",
            )
        
        logger.debug(f"Token time validations passed for user: {payload.get('sub')}")
        
        # Finally, verify the user exists and return
        admin_user = get_admin_user()
        if payload.get('sub') != admin_user.username:
            logger.warning(f"Invalid user in token from IP: {request.client.host}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid user in token",
            )
        
        return admin_user
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Token validation error from IP: {request.client.host} - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token validation failed",
        ) 