from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.database import get_db

from src.services.user_service import register_user_service, authenticate_user, test_service
from src.schemas.user_schema import UserLogin
from src.utils.jwt import get_current_user

router = APIRouter()

@router.get("/")
def test_external_api():
    """
    Тестовый эндпоинта для проверки интеграции с внешним API.
    """
    return test_service()

@router.post("/random/")
def create_random_user(db: Session = Depends(get_db)):
    """
    Берёт рандомного юзера с внешного API и добавляет в базу данных фильтрованную информацию.
    """
    return register_user_service(db)

@router.post("/auth/sign-in/")
def login_user(request: UserLogin, db: Session = Depends(get_db)):
    """
    Вход пользователя в систему с использованием email и пароля.
    Возвращает JWT токен для авторизации.
    """
    token = authenticate_user(request.email, request.password, db)
    return JSONResponse(status_code=200, content={"message": "Login successful", "Auth": token})

@router.get("/protected/")
def protected_route(current_user: str = Depends(get_current_user)):
    """
    Для проверки защищенного маршрута.
    Этот маршрут доступен только авторизованным пользователям.
    """
    return {"message": f"Hello, {current_user}! You have access to this route."}