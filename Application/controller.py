from flask import Flask , render_template , url_for, request, redirect , send_from_directory , session
from datetime import datetime
from werkzeug.utils import secure_filename
import os

from io import TextIOWrapper
app = Flask(__name__)

""" Fonctions de tri et base de données"""
from .utils import bilan_total_scientifique,dico_final

#Session
SESSION_TYPE = 'redis'
app.config['SECRET_KEY']='secret_key'

#Module csv
import pandas as pd
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
        session['fichier_csv'] = secure_filename(file.filename)
        path = os.getcwd()
        file.save(os.path.join(path,file.filename))
        session['file_is_uploaded'] = True 
        return render_template("parametre.html", fichier_csv = session.get('fichier_csv'))
    return render_template("home.html", message="Pas de fichier CSV")

"""
🟢 Page affichant les étudiants avant la sélection (Session)
🟢 Création de la session , l'utilisateur pourra modifier les param tout en pouvant revenir à la page d'origine
🟠 L'utilisateur aura un bouton 'Cliquez ici pour définir les paramètres' le renvoyant vers la page 'parametre.html'
"""
@app.route("/listeCandidat/")
@app.route("/listeCandidat/<fichier_csv>")
def listeCandidat(fichier_csv=None):
    if 'file_is_uploaded' in session:
        fichier = session.get('fichier_csv')
        data = pd.read_csv(fichier,sep = ";")
        dico = {}
        i=0
        for elem in data.Numéro:
            dico[elem] = data.Nom[i]
            i+=1
        return render_template("listeCandidat.html" , fichier_csv = session.get('fichier_csv') , dico = dico)
    return render_template("listeCandidat.html")


@app.route("/parametre/" , methods = ["GET","POST"])
def parametre():
    return render_template("parametre.html")

@app.route("/resultat/", methods = ["GET","POST"])
def resultat():
    if 'file_is_uploaded' in session:
        req = request.form
        listeMatiere = []
        math = req.get("Math")
        pc = req.get("PC")
        svt = req.get("SVT")
        bac = req.get("Bac")
        fichier = session.get('fichier_csv')
        if math == "Math": 
            listeMatiere.append(math)
        if pc == "PC": 
            listeMatiere.append(pc)
        if svt == "SVT": 
            listeMatiere.append(svt)

        if req.get("poidsNoteMath") != "":
            poidsNoteMath = int(req.get("poidsNoteMath"))
        else :
            poidsNoteMath = 3
        if req.get("poidsClassementMath") != "":
            poidsClassementMath = int(req.get("poidsClassementMath"))
        else :
            poidsClassementMath = 2
        
        if req.get("poidsNotePC") != "":
            poidsNotePC = int(req.get("poidsNotePC"))
        else :
            poidsNotePC = 3
        if req.get("poidsClassementPC") != "":
            poidsClassementPC = int(req.get("poidsClassementPC"))
        else :
            poidsClassementPC = 2
    
        if req.get("poidsNoteSVT") != "":
            poidsNoteSVT = int(req.get("poidsNoteSVT"))
        else :
            poidsNoteSVT = 3
        if req.get("poidsClassementSVT") != "":
            poidsClassementSVT = int(req.get("poidsClassementSVT"))
        else :
            poidsClassementSVT = 2
        
        bilan_total_scientifique(listeMatiere, poidsNoteMath, poidsClassementMath, poidsNotePC, poidsClassementPC, poidsNoteSVT, poidsClassementSVT, bac, fichier)
        data = pd.read_csv("fichier_traite.csv",sep = ";")
        dico = dico_final("fichier_traite.csv")
        liste_colonnes = data.columns.tolist()
        return render_template("resultat.html" , fichier_csv = session.get('fichier_csv') ,liste_colonnes = liste_colonnes ,dico = dico)
    return render_template("resultat.html", dico = {})














