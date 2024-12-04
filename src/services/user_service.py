from passlib.context import CryptContext
from src.repositories.user_repository import create_user
from sqlalchemy.orm import Session
from src.utils.jwt import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user_service(db: Session):
    return create_user(db)
        
def authenticate_user(self, email: str, password: str):
    user = self.repository.get_user_by_email(email)
    if user and pwd_context.verify(password, user.password):
        return create_access_token({"sub": user.email})
    return None
