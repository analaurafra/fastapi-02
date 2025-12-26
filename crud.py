# crud.py

fake_users_db = []

def create_user(user):
    fake_users_db.append(user)
    return user

def get_users():
    return fake_users_db

def get_user_by_email(email: str):
    for user in fake_users_db:
        if user.email == email:
            return user
    return None
