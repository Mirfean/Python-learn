from sqlalchemy.orm import sessionmaker


from sql_alchemy_tutorial import db_connect as db

# Stworzenie nowej sesji
Session = sessionmaker(bind=db.engine)
session = Session()

# dodanie danych
lebanase = db.Cucumber('Lebanase', 6, "Good for salad but really bland")
pickle = db.Cucumber('Pickle', 7, "Sour and good")
curry = db.Cucumber('Curry pickle', 8, "Salty and sweet, pretty decent")
dill = db.Cucumber('Dill pickle', 10, "God creation, Caesar of pickles")

session.add(lebanase)
session.add(pickle)
session.add(curry)
session.add(dill)

# zapis zmian w bazie danych
session.commit()
