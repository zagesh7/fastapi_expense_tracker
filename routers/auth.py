from fastapi import APIRouter,Depends,HTTPException,status
from schemas.auth import LoginRequest,LoginResponse
from sqlalchemy.orm import Session
from core.database import get_db
from models.user import User
from schemas.user import UserResponse
from core.security import verify_password
from core.jwt_helper import create_access_token

auth_router=APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@auth_router.post("",response_model=LoginResponse)
def login_user(request:LoginRequest,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==request.username).first()
    if not user or not verify_password(user.hashed_password,request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    access_token=create_access_token(
        data={
            "sub":str(user.id),
            "username":user.username
        }
    )

    return LoginResponse(access_token=access_token,user=UserResponse.model_validate(user))