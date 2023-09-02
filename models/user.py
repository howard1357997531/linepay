from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)#設定它為主鍵
    nick_name = Column(String)#unique=True代表是不可以重複的
    image_url= Column(String(length=256))#用戶的line名稱
    created_time = Column(DateTime, default=func.now())#大頭貼的url
    orders = relationship('Orders', backref='user')

    # user.orders 未來只要用這個指令就可以知道user所有的訂單
    # [<Order 1>, <>Order 2]
    
    # order.user 透過訂單就可以知道是哪個user
    # <user>
