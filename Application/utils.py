import random

from Application.models import Content,Dictionnaire

def find_nom(ine):
    res = Content.query.filter_by(ine=ine).first()
    return res