from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def primer_challenge():
    return render_template("index.html")

