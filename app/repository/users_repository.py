from sqlalchemy.orm import Session
from app.models.user_entity import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, phone_number: str) -> User:
        new_user = User(username=username, email=email, phone_number=phone_number)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()