from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr 
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr 
    password: str
    
class UserUpdate(BaseModel):
    username: str
    email: EmailStr 


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr 
    model_config = ConfigDict(from_attributes=True)
