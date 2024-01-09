from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


# создаем движок SqlAlchemy

engine = create_engine("sqlite:///films.db")

class Base(DeclarativeBase):
    pass

class Films(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    year = Column(Integer)
    gerne = Column(String)
    rating = Column(Float)

Base.metadata.create_all(bind = engine)

def create_film(name, year, gerne, rating):
    with Session(bind=engine,autoflush=False) as db:
        new_film = Films(name=name, year=year,gerne=gerne,rating=rating)
        db.add(new_film)
        db.commit

    create_film('Titanic',1997, "melodrama",8.4)
    create_film('Kaplan v kino',2023,"Horror",10.0)

def show_films(name):
    with Session(bind=engine, autoflush=False) as db:
        all_films = db.query(Films).all()
        for film in all_films:
            print(film.name,":", film.year,":",film.reating)

def show_film_of_year(year):
    with Session(bind=engine, autoflush=False) as db:
        film = db.query(Films).filter(Films.year == year).first()
        print(film.name, film.reating)

def update_film(name, new_rating):
    with Session(bind=engine, autoflush=False) as db:
        film = db.query(Films).filter(Films.name == name).first()
        if film != None:
            print(film.name, "-", film.reating)
            film.rating = new_rating
            db.commit()
        else:
            print('Фильм с таким именем не найден')
def delete_film(name, new_rating):
    with Session(bind=engine, autoflush=False) as db:
        film = db.query(Films).filter(Films.name == name).first()
        if film != None:
            db.delete(film)
            db.commit()
        else:
            print('Фильм с таким именем не существует')

show_film_of_year(1997)
update_film("Tiyanic", 10.0)
show_film_of_year(1997)
delete_film("Titanic")







