from pydantic import BaseModel,Field
from .user import UserResponse

class LoginRequest(BaseModel):
    username:str=Field(...)
    password:str=Field(...)

class LoginResponse(BaseModel):
    access_token:str
    user:UserResponse