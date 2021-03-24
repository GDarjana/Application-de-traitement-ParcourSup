from flask import Flask , render_template , url_for, request
from datetime import datetime


import re



app = Flask(__name__)

app.config.from_object('config')

from .utils import description_aleatoire
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html",
        name="Bernard",
    )

    # New functions
#Teste pour URL dynamiques

@app.route("/about/")
def about():
    return render_template("about.html",
        nature = request.args.get('nature'),
        nom = request.args.get('nom'),
        prenom = description_aleatoire(nature).prenom,

    )

@app.route("/contact/")
def contact():
    return render_template("contact.html")



#Commentaire teste
