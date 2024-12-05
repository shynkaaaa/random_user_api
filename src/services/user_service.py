from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.repositories.user_repository import create_user, get_user_by_email, main_api, get_all_registered_users, get_user_by_id, update_user_repo, delete_user_repo
from src.utils.jwt import create_access_token
from src.schemas.user_schema import UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def test_service():
    return main_api()

def register_user_service(db: Session):
    response = main_api()
    return create_user(response, db)
        
def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email, db)

    if user and pwd_context.verify(password, user.password):
        return create_access_token({"sub": user.email})
    
    return HTTPException(status_code=400, detail="Invalid email or password.")

def get_all_users_service(db: Session):
    return get_all_registered_users(db)

def update_user_service(request: UserUpdate, db: Session):
    user = get_user_by_id(request.id, db)
    return update_user_repo(request, user, db)

def delete_user_by_id(id: int, db: Session):
    if not delete_user_repo(id, db):
        return HTTPException(status_code=404, detail="No such user to delete is found.")