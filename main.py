from fastapi import FastAPI
from schemas import UserCreate
import crud

app = FastAPI()

@app.post("/users")
def create_user(user: UserCreate):
    return crud.create_user(user)

@app.get("/users")
def list_users():
    return crud.get_users()

