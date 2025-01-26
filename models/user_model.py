from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    __username = Column('username', String(32), unique=True, nullable=False, index=True)
    email = Column('email', String(200), unique=True, nullable=False)
    __password = Column('password', String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), default=func.now(), onupdate=func.now())
    
    def __init__(self, schema):
        for key, value in schema.items():
            if(hasattr(self, key)):
                setattr(self, key, value)
                
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        ### add more logical for security
        self.__username = username     
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password
                