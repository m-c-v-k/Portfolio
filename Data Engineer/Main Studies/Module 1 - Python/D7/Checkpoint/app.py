from flask import *
import datetime
import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="phonelist",
        user="postgres",
        password="MisoDaisy")

    return conn


def read_phonelist():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()

    return rows


def read_phone(name):
    cur = conn.cursor()
    print(f"SELECT phone FROM phonelist WHERE name = '{name}';")
    cur.execute(f"SELECT phone FROM phonelist WHERE name = '{name}';")
    rows = cur.fetchall()
    cur.close()

    return rows


def read_name(phone):
    cur = conn.cursor()
    print(f"SELECT name FROM phonelist WHERE phone = '{phone}';")
    cur.execute(f"SELECT name FROM phonelist WHERE phone = '{phone}';")
    rows = cur.fetchall()
    cur.close()

    return rows


def add_phone(name, phone):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.execute("COMMIT;")
    cur.close()

    return name


def delete_phone(name):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.execute("COMMIT;")
    cur.close()

    return name


def get_date():
    now = datetime.datetime.now()
    today = [str(now.year % 100), str(now.month), str(now.day)]
    if len(today[1]) < 2:
        today[1] = '0'+today[1]
    if len(today[2]) < 2:
        today[2] = '0'+today[2]

    return today


conn = connect_db()
app = Flask(__name__)


@app.route("/")
def start():
    return render_template('list.html', list=read_phonelist(), date=get_date())


@app.route("/delete", methods=['POST', 'GET'])
def delete_func():
    if request.method == 'POST':
        name = request.form['del_name']
        return render_template('delete.html', name=delete_phone(name))
    else:
        render_template('list.html')


@app.route("/insert", methods=['POST', 'GET'])
def insert_func():
    if request.method == 'POST':
        name = request.form['inp_name']
        phone = request.form['inp_phone']
        return render_template('insert.html', name=add_phone(name, phone))
    else:
        render_template('list.html')


@app.route("/api")
def api_func():
    args = request.args
    action = args.get('action', default="Bad action", type=str)
    if action == "Bad action":
        return render_template('api_usage.html', action=action)
    if action == 'phone':
        name = args.get('name', default="No name", type=str)
        if name == "No name":
            return render_template('api_usage.html', action=action)
        phone = read_phone(name)
        if len(phone) < 1:
            return f"not found {name}"
        return phone[0][0]
    if action == 'name':
        phone = args.get('phone', default="No number", type=str)
        if phone == "No number":
            return render_template('api_usage.html', action=action)
        name = read_name(phone)
        if len(name) < 1:
            return f"not found {phone}"
        return phone
    else:
        return f"Unknown action: '{action}'"


@app.route("/api_search", methods=['POST', 'GET'])
def api_search():
    if request.method == 'POST':

        inp = request.form['api_search']

        if inp.isalnum():
            action = 'phone'
        else:
            action = 'name'

        if action == "Bad action":
            return render_template('api_search.html', value="Bad inp")
        if action == 'phone':
            name = inp
            if name == "No name":
                return render_template('api_search.html', value="No name")
            phone = read_phone(name)
            if len(phone) < 1:
                return render_template('api_search.html', value="Name not found")
            return render_template('api_search.html', value=phone[0][0])
        if action == 'name':
            phone = inp
            if phone == "No number":
                return render_template('api_search.html', value="No number")
            name = read_name(phone)
            if len(name) <= 1:
                return render_template('api_search.html', value="Number not found")

            return render_template('api_search.html', value=name[0][0])
        else:
            return f"Unknown action: '{action}'"
