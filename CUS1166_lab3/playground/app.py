import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
app.config.from_object(Config)

@app.route("/")
def index():

    courses = Course.query.all()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
