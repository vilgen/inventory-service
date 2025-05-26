from datetime import timedelta
from fastapi import HTTPException, status
from .models import UserInDB, User
from .utils import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from .dependencies import fake_users_db, get_user

class AuthService:
    @staticmethod
    def authenticate_user(username: str, password: str) -> UserInDB:
        user = get_user(username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_user_token(user: UserInDB) -> str:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, 
            expires_delta=access_token_expires
        )
        return access_token

    @staticmethod
    def register_user(username: str, password: str, email: str, full_name: str = None) -> User:
        if username in fake_users_db:
            raise HTTPException(
                status_code=400,
                detail="Username already registered"
            )
        
        hashed_password = get_password_hash(password)
        user_data = {
            "username": username,
            "email": email,
            "full_name": full_name,
            "hashed_password": hashed_password,
            "disabled": False,
        }
        fake_users_db[username] = user_data
        return User(**user_data)