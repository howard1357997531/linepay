from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship
from .database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)#設定它為主鍵
    nick_name = Column(String)#unique=True代表是不可以重複的
    image_url= Column(String(length=256))#用戶的line名稱
    created_time = Column(DateTime, default=func.now())#大頭貼的url

