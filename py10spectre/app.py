
import json

from flask import Flask, render_template, request

main = 'C://Users//mksse//PycharmProjects//py10spectre//templates//main.html'
index = 'C://Users//mksse//PycharmProjects//py10spectre//templates//index.html'


app = Flask(__name__.split('.')[0])
print(f'***** Uruchomiono serwer z aplikacji: "{app}" ******')


def read_db():
    with open("db.json", "r") as file:
        content = json.loads(file.read())
        return content


def write_db(content):
    with open("db.json", "w") as file:
        file.write(json.dumps(content, indent=4))


@app.route('/main/', methods=["GET", "POST"])
def main():
    content = read_db()
    if request.method == 'POST':
        content.append({'name':         request.form['name'],
                       'profession':   request.form['profession']})
        write_db(content)
    # wyświetla parametry w pasku adresu:
    # print(request.args["name"])
    # print(request.form["name"]), request.form["profession"]
    return render_template('main.html', content=content)


@app.route('/')
def welcome():
    content = read_db()
    return render_template('index.html', content=content)
    # return '\n'.join(row['name'] for row in content)


@app.route("/names/<name>")
def welcome_somebody(name):
    content = read_db()
    for row in content:
        if row["name"] != name:
            continue
        return row["profession"]
    return "Nie znaleziono."


# if __name__ == '__main__':
#     print('Blablabla...')

