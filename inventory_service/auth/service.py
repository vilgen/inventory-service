from datetime import timedelta
from fastapi import HTTPException, status
from .models import User
from .utils import create_access_token
from .dependencies import authenticate_user
from inventory_service.config.auth_settings import auth_settings
from fastapi import Response  

class AuthService:
    @staticmethod
    def login_user(username: str, password: str) -> dict:
        """Authenticate user and return token"""
        user = authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, 
            expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    
    @staticmethod
    def login_user_cookie(response: Response, username: str, password: str) -> dict:
        """NEW: Cookie-based login - stores JWT in HttpOnly cookie"""
        user = authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
        
        # Create JWT token (same logic as original)
        access_token_expires = timedelta(minutes=auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, 
            expires_delta=access_token_expires
        )
        
        # Store JWT in HttpOnly cookie instead of returning it
        response.set_cookie(
            key="access_token",
            value=access_token,
            max_age=auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # Convert to seconds
            httponly=True,    # Cannot be accessed by JavaScript (XSS protection)
            secure=False,     # Set to True in production with HTTPS
            samesite="lax",   # CSRF protection
            path="/"          # Cookie available for entire domain
        )
        
        return {
            "message": "Login successful",
            "username": user.username,
            "expires_in_minutes": auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES
        }