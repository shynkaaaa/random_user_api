from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import JSON

from src.models import User
from src.schemas.user_schema import UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(response: JSON, db: Session):
    data = response["results"][0]

    plain_password = data["login"]["password"]
    hashed_password = pwd_context.hash(plain_password)

    user = User(
        first_name=data["name"]["first"],
        last_name=data["name"]["last"],
        age=data["dob"]["age"],
        email=data["email"],
        password=hashed_password, 
        gender=data["gender"],
        country=data["location"]["country"],
        city=data["location"]["city"]
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)

    user.password = plain_password

    return user

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()

def get_all_registered_users(db: Session):
    return db.query(User).all()

def update_user_repo(request: UserUpdate, user: User, db: Session):
    if request.first_name is not None:
        user.first_name = request.first_name
    if request.last_name is not None:
        user.last_name = request.last_name
    if request.age is not None:
        user.age = request.age
    if request.email is not None:
        user.email = request.email
    if request.gender is not None:
        user.gender = request.gender
    if request.country is not None:
        user.country = request.country
    if request.city is not None:
        user.city = request.city
    
    db.commit()
    db.refresh(user)
    return user

def delete_user_repo(id: int, db: Session):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return True