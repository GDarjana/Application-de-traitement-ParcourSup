import os
from flask import Flask

from .controller import app

app.static_folder = 'static'