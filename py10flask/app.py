# ACCOUNTANT v2.0 on classes
# -*- coding: UTF-8 -*-                                                        #
# "accountant" obiektowo, wyłącznie z obsługą plików we/wy                     #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  #
import json
# from lib.acc_cls import Reader, Manager
from flask import Flask, render_template, url_for, request
# from flask_jsondash.charts_builder import charts
# - - - - - - - A C C O U N T A N T   I N   H T M L - - - - - - - - - - - - - -#


app = Flask(__name__.split('.')[0])
print(f'**** Uruchomiono serwer z aplikacji >>> {app} ******')


def read_db():
    with open("db.txt", "r") as file:
        content = json.loads(file.read())
        return content


def write_db(content):
    with open("db.txt", "w") as file:
        file.write(json.dumps(content))


@app.route("/main/")
def main():
    return render_template("main.html")


@app.route("/")
def welcome():
    content = read_db()
    return render_template("index.html", content=content)
    # return '\n'.join(row['name'] for row in content)


@app.route("/names/<name>")
def welcome_somebody(name):
    content = read_db()
    for row in content:
        if row["name"] != name:
            continue
        return row["profession"]
    return "Nie znaleziono."

