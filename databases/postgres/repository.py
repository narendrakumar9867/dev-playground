from sqlalchemy.orm import Session
from models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
        
    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    
    def get_all(self) -> list[User]:
        return self.db.query(User).all()
    
    
    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
    
    
    def update(self, user_id: int, name: str, email: str) -> User | None:
        user = self.get_by_id(user_id)
        if not user:
            return None
        
        user.name = name
        user.email = email
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    
    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if not user:
            return False
        
        self.db.delete(user)
        self.db.commit()
        
        return True
    
    