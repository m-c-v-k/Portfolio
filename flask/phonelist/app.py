from flask import Flask, request, render_template
import datetime
import psycopg2

phone_list = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def start():

    list_items(conn)
    D = get_date()
    return render_template('list.html', list=phone_list, date=D)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    return render_template('delete.html', list=phone_list)


@app.route("/insert", methods=["GET", "POST"])
def insert():
    insert(conn)
    return render_template('insert.html', list=phone_list)


def get_date():
    now = datetime.datetime.now()
    D = [str(now.year % 100), str(now.month), str(now.day)]
    if len(D[1]) < 2:
        D[1] = '0'+D[1]
    if len(D[2]) < 2:
        D[2] = '0'+D[2]

    return D


def connect():
    conn = None

    try:
        # Connect to db
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="phonelist",
            user="postgres",
            password="MisoDaisy"
        )

        print("Connected to db.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


def list_items(conn):
    command = "SELECT * FROM phonelist;"
    sql_command(conn, command)


def insert(conn):
    name = request.form.get('name')
    print(name)
    phone = request.form.get('phone')
    print(phone)
    command = f"""INSERT INTO phonelist (name, phone)
VALUES ('{name}', '{phone}');"""
    print(f"{name} Added")
    sql_command(conn, command)


def sql_command(conn, command):
    global phone_list

    try:
        cur = conn.cursor()

        if ("*" in command):
            cur.execute(f"{command}")
            rows = cur.fetchall()

            phone_list = []
            for row in rows:
                phone_list.append(row)

            cur.close()

        elif ("DELETE" in command):
            cur.execute(f"{command}")
            cur.commit()
            cur.close()

        elif "INSERT" in command:
            cur.execute(f"{command}")
            conn.commit()
            cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


conn = connect()
