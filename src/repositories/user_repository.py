import requests
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session):
    response = requests.get("https://randomuser.me/api/")
    data = response.json()["results"][0]

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

    return user
