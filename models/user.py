from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)#設定它為主鍵
    nick_name = Column(String)#unique=True代表是不可以重複的
    image_url= Column(String(length=256))#用戶的line名稱
    created_time = Column(DateTime, default=func.now())#大頭貼的url
    # 加上這段建立users跟orders之間的關聯
    # Orders第一個為關聯model class name
    orders = relationship('Orders', backref='user')

    # user.orders 未來只要用這個指令就可以知道user所有的訂單
    # [<Order 1>, <Order 2>]
    
    # order.user 透過訂單就可以知道是哪個user
    # <uSER 1>

'''
在 SQLAlchemy 中，backref 参数用于创建双向关系（bidirectional relationship），通常用于定义两个表之间的关联关系，其中一个表引用另一个表。

在给定的代码中，backref 用于创建一个双向关系，将 Users 表与另一个名为 Orders 的表关联起来。具体来说：

relationship('Orders', backref='user') 创建了一个关系，将 Users 表与 Orders 表关联起来。这意味着一个用户（Users）可以拥有多个订单（Orders）。

backref='user' 中的 'user' 是一个字符串，它表示在 Orders 表中会有一个属性，用于引用关联的用户。这个属性的名称就是 'user'，因此，每个订单对象都将有一个名为 user 的属性，该属性可以用来访问与订单相关联的用户对象。

这样，当您查询一个订单对象时，可以通过 order.user 访问该订单所属的用户对象，而不必在订单对象中显式存储用户信息，这提供了方便的双向访问。

例如，假设您有一个订单对象 order，您可以使用 order.user 访问该订单所属的用户对象，而不必编写额外的查询语句。这可以使数据模型更加清晰和易于使用。
'''
