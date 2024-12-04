from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str
    password: str
    gender: str
    country: str
    city: str

class UserResponse(User):
    id: int

class UserLogin(BaseModel):
    email: str
    password: str
