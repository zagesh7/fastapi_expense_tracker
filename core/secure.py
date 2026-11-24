from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,Request,status
from sqlalchemy.orm import Session
from core.database import get_db

security_scheme=OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(request:Request,token:str=Depends(security_scheme),db:Session=Depends(get_db)):
    from core.jwt_helper import verify_access_token
    from models.user import User

    try:
        payload=verify_access_token(token)
        user_id=payload.get("sub")
        username=payload.get("username")
        if user_id is None:
            raise HTTPException(
                detail="Invalid Token",
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        user=db.query(User).filter(User.id==int(user_id)).first()
        if user is None:
            raise HTTPException(
                detail="Invalid Token",
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        request.state.user=user
        return user
    except Exception as e:
        print(e)
        raise HTTPException(
            detail="Invalid Token",
            status_code=status.HTTP_401_UNAUTHORIZED
        )