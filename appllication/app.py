from functions import main
from flask import Flask, render_template, request, redirect, url_for, flash, g, abort,current_app,make_response, session
import os

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def home():
    return render_template()
