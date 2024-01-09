'''Создайте модели базы данных интернет магазина бытовой техники по следующей схеме, дополнительные таблицы(например для связи многие ко многим) создайте на свое усмотрение :
Таблица User:
-	Id
-	Email
-	Password
-	Role(внешний ключ отсылающий на id модели Role, у одного пользователя 1 роль
-	Orders(отношение к таблице Order, у одного пользователя много заказов)
Таблица Role:
-	Id
-	Name
-	Users(отношение к таблице User, у одной роли много пользователей
Таблица Products:
      - id
- name
- quantity
- price
- category(внешний ключ на id модели Category)
- orders(отношение к таблице Order, связь многие ко многим)
Таблица Category:
-	Id
-	Name
-	Products(отношение к таблице Products, у одного товара 1 категория, у категории много товаров)
Таблица Order:
-	Id
-	User_id(внешний ключ на id модели User)
-	Cart(отношение к таблице Products,связь многие ко многим)
-      date
-     total_price
'''

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///books.db"
engine = create_engine(sqlite_database)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    role = Column(String, ForeignKey('role.id'))
    orders = relationship("Order", back_populates="user")

class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("User", back_populates="role")

class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    products = Column(String)

class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('User.id'))
    cart = relationship(("Products", primary_key:=True))
    date = Column(String)
    total_price = Column(Integer)

class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(String)
    price = Column(String)
    category = Column(String, ForeignKey("category.id"))
    orders = relationship("Order", secondary="association")

association_table = ("association", Base.metadata,
                          Column("products.id", Integer, ForeignKey("products.id"), primary_key = True),
                          Column("order.id", Integer, ForeignKey("order.id"), primary_key=True))
with Session(autoflush=False, bind=engine) as db:
    oleg = User(name="Oleg")
    arnou = User(name="Arnou")
    kaplan = User(name="Kaplan")
    areg = User(name="Areg")
    leo = User(name="Leo")
    ron = User(name="Ron")
    harry = User(name="Harry")

    seller = Role(name="seller")
    buyer = Role(name="buyer")

    iron = Products(name="iron")
    fridge = Products(name="fridge")
    stove = Products(name="stove")
    fan = Products(name="fan")

    seller.users = [oleg]
    seller.users = [arnou]
    seller.users = [kaplan]
    seller.users = [areg]
    seller.users = [leo]
    buyer.users = [ron]
    buyer.users = [harry]


    db.add_all([seller, buyer])
    db.commit()





