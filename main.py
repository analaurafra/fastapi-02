from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Rodando :))"}

@app.post("/users/{user_id}")
def get_user(user_id: int, active: bool = True):
    return {
        "id": user_id,
        "active": active
    }
