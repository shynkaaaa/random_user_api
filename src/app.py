from fastapi import FastAPI
from src.routing import user

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}