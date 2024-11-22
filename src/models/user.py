from sqlalchemy import Column, Integer, String
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    user_name = Column(String)
    hashed_password = Column(String)

