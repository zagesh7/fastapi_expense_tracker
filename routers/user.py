from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate,UserResponse
from core.database import get_db
from models.user import User
from core.security import hash_password,verify_password

user=APIRouter(prefix="/users",tags=["users"])

@user.post("",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(request:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.username==request.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_pwd=hash_password(request.password)
    
    new_user=User(
        username=request.username,
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user