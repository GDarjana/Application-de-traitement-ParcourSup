from flask import Flask , render_template , url_for, request, redirect , send_from_directory , session
from datetime import datetime
from werkzeug.utils import secure_filename
import re
import os

app = Flask(__name__)


#Dropzone upload
from flask_dropzone import Dropzone
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.csv'


app.config.from_object('config')
app.config["DEBUG"] = True
dropzone = Dropzone(app)

#Dossier upload
#Au préalable àvoir un dossier upload dans le dossier Application
UPLOAD_FOLDER = '/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Module csv
import pandas as pd
import csv
from pandas import DataFrame,read_csv




#Routes 

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


"""
🟢 L'utilisateur sélectionne le fichier .csv et est redirigé vers 'listeCandidat.html'
🟠 Drag and drop du fichier csv
"""

# Page home
@app.route("/" , methods = ["GET","POST"])
def home():
    if request.method=="POST":
        file =  request.files["file"]
        filename = secure_filename(file.filename)
        path = os.getcwd()
        file.save(os.path.join(path,file.filename))
        data = pd.read_csv(os.path.join(path,file.filename), sep = ";")
        dico = {}
        i=0
        for elem in data.Numéro:
            dico[elem] = data.Nom[i]
            i+=1
        return render_template("listeCandidat.html", fichier_csv = filename , dico = dico)
    return render_template("home.html", message="Pas de fichier CSV")

"""
🟠 L'utilisateur aura un bouton 'Cliquez ici pour définir les paramètres' le renvoyant vers la page 'parametre.html'
🟠 Page affichant les étudiants avant la sélection (Session)
🟠 Création de la session , l'utilisateur pourra modifier les param tout en pouvant revenir à la page d'origine
"""
@app.route("/listeCandidat/")
@app.route("/listeCandidat/<fichier_csv>")
def listeCandidat(fichier_csv=None):
    return render_template("listeCandidat.html" , fichier_csv = fichier_csv , dico = dico)

@app.route("/parametre")
def parametre():
    return render_template("parametre.html")














