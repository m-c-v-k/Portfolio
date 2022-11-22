from flask import Flask, render_template, request
import datetime
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="phonelist",
        user="postgres",
        password="MisoDaisy")
    return conn


def read_phonelist():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def delete_contact(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()
    return name


def insert_contact(name, phone):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()
    return f"{name} with {phone} added!"


app = Flask(__name__)


@app.route("/")
def start_page():
    now = datetime.datetime.now()
    today = [str(now.year % 100), str(now.month), str(now.day)]
    # Padding a zero digit in front if month or day is single digit
    if len(today[1]) < 2:
        today[1] = '0'+today[1]
    if len(today[2]) < 2:
        today[2] = '0'+today[2]
    return render_template('list.html', list=read_phonelist(), date=today)


@app.route("/delete", methods=['POST', 'GET'])
def delete_page():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('delete.html', req=delete_contact(name))
    else:  # GET method
        return render_template('list.html', list=read_phonelist())

# @app.route("/insert", methods = ['POST', 'GET'])


@app.route("/insert", methods=['POST', 'GET'])
def insert_page():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        return render_template('insert.html', req=insert_contact(name, phone))
    else:  # GET method
        return render_template('list.html', list=read_phonelist())


if __name__ == '__main__':
    app.run(debug=True)
