from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routing import user
from src.database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
    
    yield  

app = FastAPI(lifespan=lifespan)

app.include_router(user.router, prefix="/users", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Здравствуйте!"}