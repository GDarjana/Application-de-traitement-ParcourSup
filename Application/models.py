from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum
import os

from .controller import app


#Create database connection object

db = SQLAlchemy(app)

#CSV Button
from flask_restful import Resource
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))





#Table Content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    ine = db.Column(db.String(50),nullable = False)

    def __init__(self,nom,prenom,gender,ine):
        self.nom = nom 
        self.prenom = prenom
        self.gender = gender
        self.ine = ine

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Jean","Pierre","Homme","KIJ463"))
    db.session.add(Content("Marie","oof","Femme","YEUO98"))
    db.session.add(Content("Mike","Nil","Autre","UJR367"))
    db.session.commit()
    lg.warning('Database initialized!')


class Dictionnaire(dict):
    def __init__(self):
        self = dict()
    
    def add(self,cle,valeur):
        self[cle] = valeur