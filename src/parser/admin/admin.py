from flask import Flask, render_template, redirect, url_for
import webbrowser
import logging
from flask import jsonify

DATABASES = []


app = Flask(__name__)



@app.route("/")
def index():
    return jsonify(DATABASES[0].dict_)

@app.route("/add/<data>")
def add(data):
    DATABASES[0].add(data)
    return redirect("/")


@app.route("/delete/<data>")
def delete(data):
    DATABASES[0].delete(data)
    return redirect("/")


def run():
    if DATABASES:
        webbrowser.open("http://localhost:5000")
        app.run(debug=False)
    else:
        logging.error("Database does'nt exists")