from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str
    password: str
    gender: str
    country: str
    city: str

class UserUpdate(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    
class UserLogin(BaseModel):
    email: str
    password: str
