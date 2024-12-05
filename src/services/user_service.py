from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.repositories.user_repository import create_user, get_user_by_email, main_api
from src.utils.jwt import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def test_service():
    return main_api()

def register_user_service(db: Session):
    return create_user(db)
        
def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email, db)

    if user and pwd_context.verify(password, user.password):
        return create_access_token({"sub": user.email})
    
    return HTTPException(status_code=400, detail="Invalid email or password.")
