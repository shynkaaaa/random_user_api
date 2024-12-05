from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.database import get_db

from src.services.user_service import register_user_service, authenticate_user
from src.schemas.user_schema import UserLogin

router = APIRouter()

@router.post("/random/")
def create_random_user(db: Session = Depends(get_db)):
    return register_user_service(db)

@router.post("/auth/sign-in/")
def login_user(request: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(request.email, request.password, db)
    return JSONResponse(status_code=200, content={"message": "Login successful", "Auth": token})