from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.database import get_db

from src.services.user_service import register_user_service

router = APIRouter()

@router.post("/random/")
def create_random_user(db: Session = Depends(get_db)):
    return register_user_service(db)