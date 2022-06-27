from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Residente_envia, Residente_recibe, Involucrado
import requests

def createapp(environment):
    app = Flask(__name__)
    app.config.from_object(environment)
    with app.app_context(): 
        db.init_app(app)
        db.create_all()
    return app

environment=config["development"]

app=createapp(environment)

@app.route("/")
def primer_challenge():
    return render_template("index.html")

