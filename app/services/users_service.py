from sqlalchemy.orm import Session
from app.repository.users_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, username: str, email: str, phone_number: str):
        return self.user_repository.create_user(username, email, phone_number)

    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)