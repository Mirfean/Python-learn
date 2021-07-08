# import obiektów z SQLAlchemy, których działanie zobaczymy z czasem
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# inicjalizacja połaczenia z bazą danych
engine = create_engine('sqlite:///P:\\Projects\\SQL\\db_to_practice.db', echo=True)

print(engine)

# obsluga zarządzania tabelami
base = declarative_base()


class Cucumber(base):
    __tablename__ = 'Cucumber'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Integer)
    description = Column(String)

    def __init__(self, name, rating, description):
        self.name = name
        self.rating = rating
        self.description = description


# Creating table
base.metadata.create_all(engine)
