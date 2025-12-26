from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
from loguru import logger
import time

print(">>> SANITY CHECK: MAIN CARREGADO <<<")

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return user

@app.middleware("http")
async def log_requests(request: Request, call_next):
    body = await request.body()
    logger.info(f"Request {request.method} {request.url} Body: {body.decode('utf-8')}")
    response = await call_next(request)
    logger.info(f"Response status_code={response.status_code} for {request.method} {request.url}")
    return response

