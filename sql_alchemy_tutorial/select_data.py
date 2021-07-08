from sql_alchemy_tutorial import db_connect as db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

# wszystkie dane
for s in session.query(db.Cucumber).all():
    print(s.id)

# wybrane transakcje
for s in session.query(db.Cucumber).filter(db.Cucumber.rating > 7):
    print(s.name)