from flask import Flask, render_template, request
import MySQLdb
import django
import json
from acc_class import Reader, Manager

path = "C:/Users/mksse/PycharmProjects/py11sql/"
db_acc = path + "source/db.json"
with open ('lib/access_db.txt', mode='r', encoding='utf-8') as file:
    hostname = str(file.readline()).strip()
    username = str(file.readline()).strip()
    password = str(file.readline()).strip()

conn = MySQLdb.connect(hostname, username, password)
cursor = conn.cursor()


app = Flask(__name__.split('.')[0])
print(f'***** Uruchomiono serwer z aplikacji: "{app}" ******')


def read_db():
    with open(db_acc, "r") as file:
        content = json.loads(file.read())
        return content


def write_db(content):
    with open(db_acc, "w") as file:
        file.write(json.dumps(content, indent=4))


@app.route('/', methods=["GET", "POST"])
def hello():
    content = read_db()
    if request.method == 'POST':
        if id(button) == 'button1':     # S A L D O
            content.append({'saldo': request.form['saldo'],
                            'comment': request.form['comment']})
            write_db(content)
            
        if id(button) == 'button2':     # Z A K U P
            content.append({'item': request.form['item'],
                            'price': request.form['price'],
                            'quantity': request.form['qty']})
            
        if id(button) == 'button3':     # S P R Z E D A Ż
            content.append({'item': request.form['item'],
                            'price': request.form['price'],
                            'quantity': request.form['qty']})
        if id(button) == 'button4':     # P R Z E G L Ą D
            pass
        if id(button) == 'button5':     # M A G A Z Y N
            pass

    return render_template('main.html', content=content)






from accountant import manager
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #test db to nazwa pliku w którym utworzymy bazę danych

db = SQLAlchemy(app)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    what_action = db.Column(db.String(12), unique=False)
    first_action = db.Column(db.Integer, unique=False)
    second_action = db.Column(db.String(120), unique=False)
    third_action = db.Column(db.Integer, unique=False)


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(64), unique=True)
    qty = db.Column(db.Integer, unique=False)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, unique=False, nullable=False)


# db.create_all()
alembic = Alembic()
alembic.init_app(app)


@app.route("/", methods=["GET", "POST"])
def welcome():
    stock = db.session.query(Stock).all()
    funds = db.session.query(Account).filter(Account.id == 1).first()
    money = funds.account if funds else 0
    return render_template("index.html", stock=stock, account=money)


@app.route("/saldo/", methods=["GET", "POST"])
def balance():
    funds = db.session.query(Account).filter(Account.id == 1).first()
    if request.method == "POST":
        if funds.account + int(request.form["Kwota"]) < 0:
            raise Exception("Niewystarczające środki.")
        log = History(
            what_action="saldo",
            first_action=request.form["Kwota"],
            second_action=request.form["Komentarz"],
            third_action=None
        )
        funds.account += int(request.form["Kwota"])
        db.session.add(log)
        db.session.add(funds)
        db.session.commit()
        return redirect("/")
    return render_template("saldo.html")



@app.route("/zakup/", methods=["GET", "POST"])
def buy():
    funds = db.session.query(Account).filter(Account.id == 1).first()
    if request.method == "POST":
        if funds.account - (int(request.form["Cena"]) * int(request.form["Ilosc"])) < 0:
            raise Exception("Niewystarczające środki.")
        purchase = Stock(
            product=request.form["Produkt"],
            qty=request.form["Ilosc"]
        )
        db.session.add(purchase)
        funds.account -= (int(request.form["Cena"]) * int(request.form["Ilosc"]))
        db.session.add(funds)
        log = History(
            what_action="zakup",
            first_action=request.form["Produkt"],
            second_action=request.form["Cena"],
            third_action=request.form["Ilosc"]
        )
        db.session.add(log)
        db.session.commit()
        return redirect("/")
    return render_template("zakup.html")


@app.route("/sprzedaz/", methods=["GET", "POST"])
def sell():
    if request.method == "POST":
        stock = db.session.query(Stock).filter(Stock.product == request.form["Produkt"]).first()
        if stock.product != request.form["Produkt"]:
            raise Exception("Brak towaru w magazynie.")
        funds = db.session.query(Account).filter(Account.id == 1).first()
        stock.qty -= int(request.form["Ilosc"])
        funds.account += (int(request.form["Cena"]) * int(request.form["Ilosc"]))
        db.session.add(funds)
        log = History(
            what_action="sprzedaz",
            first_action=request.form["Produkt"],
            second_action=request.form["Cena"],
            third_action=request.form["Ilosc"]
        )
        db.session.add(log)
        db.session.commit()
        return redirect("/")
    return render_template("sprzedaz.html")


@app.route("/historia/")
@app.route("/historia/<od>/")
@app.route("/historia/<od>/<do>/")
def history(od=None, do=None):
    if od and do:
        content = db.session.query(History).filter(History.id >= od).filter(History.id <= do).all()
    elif not do and od:
        content = db.session.query(History).filter(History.id >= od).all()
    else:
        content = db.session.query(History).all()
    return render_template("historia.html", content=content)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
    