from fastapi import APIRouter, Depends, Form, Request, Response
from inventory_service.models.auth import Token, User
from inventory_service.middleware.auth_dependencies import (
    get_current_active_user,
    get_current_user,
    get_current_user_from_cookie
)
from inventory_service.services.auth_service import AuthService

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

@auth_router.post("/login", response_model=Token)
async def login(username: str = Form(), password: str = Form()):
    return AuthService.login_user(username, password)

@auth_router.get("/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    return current_user

@auth_router.get("/users", response_model=User)
async def get_all_user_info(all_user: User = Depends(get_current_user)):
    return all_user

@auth_router.post("/login-cookie")
async def login_cookie(
    response: Response,
    username: str = Form(), 
    password: str = Form()
):
    """NEW: Cookie-based login - stores JWT in HttpOnly cookie"""
    return AuthService.login_user_cookie(response, username, password)

@auth_router.get("/me-cookie", response_model=User)
async def get_current_user_cookie(
    current_user: User = Depends(get_current_user_from_cookie)
):
    """NEW: Cookie-based user info - reads JWT from cookie"""
    return current_user

@auth_router.post("/logout-cookie")
async def logout_cookie(response: Response):
    """NEW: Clear authentication cookie"""
    response.delete_cookie("access_token")
    return {"message": "Logout successful"}

@auth_router.get("/inventory-cookie")  
async def get_inventory_cookie(current_user: User = Depends(get_current_user_from_cookie)):
    return {
        "message": f"Inventory accessed by {current_user.full_name}",
        "items": ["item1", "item2", "item3"],
        "auth_method": "JWT Cookie"
    }

@auth_router.get("/protected-cookie")
async def protected_route_cookie(current_user: User = Depends(get_current_user_from_cookie)):
    """NEW: Cookie-based protected route demo"""
    return {
        "message": f"Hello {current_user.full_name}, welcome to the inventory system!",
        "user": current_user.username,
        "admin": current_user.is_admin,
        "auth_method": "JWT Cookie"
    } 