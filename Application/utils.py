import random

from Application.models import Content, Nature

def description_aleatoire(nature):
    contenu = Content.query.filter(Content.nature == Nature[nature]).all()
    return random.choice(contenu)