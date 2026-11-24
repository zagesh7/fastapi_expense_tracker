from fastapi import FastAPI,Depends
from core.database import Base,engine
from routers.user import user
from routers.auth import auth_router
from models.user import User
from core.secure import get_current_user
from sqlalchemy.orm import Session
from core.database import get_db

app=FastAPI()
app.include_router(user)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home(db:Session=Depends(get_db),user:User=Depends(get_current_user)):
    return {"Welcome"}
