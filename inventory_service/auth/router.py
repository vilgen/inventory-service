from fastapi import APIRouter, Depends, HTTPException, status, Form
from .models import Token, User
from .dependencies import get_current_active_user
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/login", response_model=Token)
async def login(username: str = Form(), password: str = Form()):
    user = AuthService.authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = AuthService.create_user_token(user)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
async def register(
    username: str = Form(), 
    password: str = Form(), 
    email: str = Form(),
    full_name: str = Form(None)
):
    return AuthService.register_user(username, password, email, full_name)

@router.get("/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    return current_user
