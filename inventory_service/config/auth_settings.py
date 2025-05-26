from pydantic_settings import BaseSettings

class AuthSettings(BaseSettings):
    SECRET_KEY: str ="123123123123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    ADMIN_EMAIL: str
    ADMIN_FULL_NAME: str
    
    class Config:
        env_file = ".env"

auth_settings = AuthSettings()