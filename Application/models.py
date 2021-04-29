from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app

#Create database connection object

db = SQLAlchemy(app)



class Nature(enum.Enum):
    femme = 0
    homme = 1
    alien = 2



#Table Content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    nature = db.Column(db.Enum(Nature), nullable=False)

    def __init__(self,nom,prenom,nature):
        self.nom = nom 
        self.prenom = prenom
        self.nature = nature

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Jean Rene","Tu sais deja",Nature['femme']))
    db.session.add(Content("Katoun","Fieuu",Nature['femme']))
    db.session.add(Content("Aouhh","Pas dpiece?",Nature['alien']))
    db.session.commit()
    lg.warning('Database initialized!')

