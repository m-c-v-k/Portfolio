# Importing necessary libraries
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/salmonAndSpinach")
def salmonAndSpinach():
    return render_template('salmonAndSpinach.html')
