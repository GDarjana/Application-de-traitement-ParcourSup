# Application-de-traitement-ParcourSup

Application traitant les demandes ParcourSup 

Création de l'environnement de travail:

(En fonction de la version de python installé, la commande python peut varier en py)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Linux
sudo apt-get install python3-venv    
python3 -m venv env

# macOS
python3 -m venv env

# Windows
python -m venv env

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Activation de l'environnement de travail:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# macOS / Linux
source env/bin/activate

# Windows
.\env\Scripts\activate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Installation de la dernère version de Python
- Langage de programmation interprété
  - Dernière version 3.9.5 (3 mai 2021)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

python -m pip install --upgrade pip

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Installation de la dernière version de Flask
- Framework de développement web en Python
  - Serveur de développement
  - Moteur de template pour format HTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

python -m pip install flask

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Installation de la dernière version de Panda
- Manipulation d'objet de type DataFrame
  - Fichier csv
  - Fichier excel
  - Fichier textuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pip install pandas

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Installation de la dernière version de Werkzeug
- Librairie d'application web
  - Utilitaire HTTP
  - Traitement de cookies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pip install -U Werkzeug

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Désactivation de l'environnement de travail:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# macOS / Linux / Windows
deactivate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
