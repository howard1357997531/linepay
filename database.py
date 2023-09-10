from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists

import os
current_dir = os.path.dirname(__file__) #透過os取得目前的路徑
db_path = r'sqlite:///{}/lstore.db'.format(current_dir)
engine = create_engine(db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# 为 Base 类添加一个属性 query，使得该类的实例可以使用 db_session 来执行查询。
Base.query = db_session.query_property()

def init_db():
    if database_exists(db_path):
        return False
    else:
        Base.metadata.create_all(engine)
        # Base.metadata.create_all(bind = engine)
        return True

# 全部解釋
'''
这段代码是使用 SQLAlchemy 库来连接和初始化 SQLite 数据库的代码。以下是对代码中各个部分的详细解释：

首先，导入了所需的模块和类，包括 create_engine、scoped_session、sessionmaker、declarative_base 
以及 database_exists。这些模块和类用于创建数据库引擎、数据库会话，以及数据库模型。

使用 os 模块获取当前文件所在的目录，这个目录将用于构建 SQLite 数据库文件的路径。

构建数据库路径 db_path，这个路径指向一个名为 lstore.db 的 SQLite 数据库文件，位于当前文件所在目录下。
db_path 使用了字符串格式化，将当前目录路径插入到字符串中。

使用 create_engine 函数创建一个 SQLAlchemy 引擎 engine，并指定连接的数据库是 SQLite，传入了 db_path 作为连接字符串。
convert_unicode=True 参数用于处理字符编码。

创建一个数据库会话 db_session，使用 scoped_session 和 sessionmaker 来创建。这个会话将用于执行数据库操作。

创建一个基本的声明类 Base，它是 SQLAlchemy 的 declarative_base 的实例，用于定义数据库模型类。

为 Base 类添加一个属性 query，使得该类的实例可以使用 db_session 来执行查询。

定义了一个名为 init_db 的函数，用于初始化数据库。这个函数首先检查数据库是否已经存在，如果存在则返回 False，
否则创建数据库表结构并返回 True。

总结起来，这段代码的主要作用是连接到 SQLite 数据库，创建一个数据库会话，定义了一个基本的声明类，
以及提供了一个初始化数据库的函数。当调用 init_db 函数时，它会创建数据库表结构，但仅在数据库文件不存在的情况下执行。
这是一个常见的数据库初始化操作，通常用于确保数据库表在应用程序启动时已经存在。
'''
    
# 解釋 db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
'''
在 SQLAlchemy 中，scoped_session 和 sessionmaker 用于创建数据库会话对象，而其中的参数 autocommit 和 autoflush 
控制数据库会话的行为。

autocommit=False：

当 autocommit 设置为 False 时，表示数据库会话不会自动提交事务。这意味着您需要明确调用 commit() 方法来提交您在会话中所做的更改到数据库。
这通常用于在一个事务中执行多个数据库操作，然后一次性提交这些操作，以确保数据的一致性。
如果 autocommit 设置为 True，则每个数据库操作都会自动提交，这可能导致不必要的事务开销和潜在的数据不一致。
autoflush=False：

autoflush 控制数据库会话在查询数据库时是否自动执行 flush 操作。flush 操作会将尚未提交的更改刷新到数据库中。
当 autoflush 设置为 False 时，数据库会话不会自动执行 flush 操作。这可以提高性能，因为您可以延迟将更改刷新到数据库，直到您明确要求时才执行。
但是，如果不小心，这也可能导致数据不一致，因为您可能在查询中看到尚未提交的更改。
如果 autoflush 设置为 True，则在查询数据库时，会自动执行 flush 操作，以确保查询结果反映最新的数据状态。
在给定的代码中，db_session 使用了这两个参数，autocommit=False 和 autoflush=False。这意味着它是一个非自动提交的数据库会话，
并且不会自动执行 flush 操作。这通常用于需要更精确地控制事务的情况，以及在需要在多个操作之间共享数据库会话的情况下。在这种情况下，
您需要显式地调用 commit() 来提交更改，并在需要时手动执行 flush 操作。
'''