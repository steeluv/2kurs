"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///books.db"
engine = create_engine(sqlite_database)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    book = relationship("Book", back_populates="users")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    book_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="book")

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    sherlok_holms = Book(name = "Sherlok Holms")
    taras_bulba = Book(name = "Taras Bulba")
    bednaya_liza = Book(name = "Bednaya Liza")

    arnou = User(name = "Arnou")
    makson = User(name = "Makson")

    arnou.book=[sherlok_holms]
    arnou.book=[taras_bulba]
    makson.book=[bednaya_liza]

    db.add_all([arnou, makson])
    db.commit()


with Session(autoflush=False, bind=engine) as db:
    users = db.query(User).all()
    for u in users:
        print(f"{u.name} ({u.book.name}")

