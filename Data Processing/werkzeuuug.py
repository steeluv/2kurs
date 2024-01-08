from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine("sqlite:///users.db")

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)

def signup():
    print('-----------Регистрация------------')
    username = input('Введите логин: ')
    password = input("Введите пароль: ")
    user = User(username=username,password=generate_password_hash(password))
    with Session(bind=engine,autoflush=False) as db:
        db.add(user)
        db.commit()
        print('Регистрация прошла успешно')
    signin()

def signin():
    print('----------Авторизация-----------')
    username = input('Введите логин: ')
    password = input('Введите пароль: ')
    with Session(bind = engine, autoflush = False) as db:
        user = db.query(User).filter(User.username == username).first()
        if user == None:
            print('Пользователь с указанным username не найден')
        else:
            if check_password_hash(user.password,password):
                print('Вы успешно авторизованы')
            else:
                print('Пароль не подходит')


answer = input('Добро пожаловать! \nВведите 1 - для регистрации.\nВведите 2 - для авторизации.\n')
if answer == '1':
    signup()
elif answer == '2':
    signin()
else:
    print('Действие не обнаружено, перезапустите программу')







