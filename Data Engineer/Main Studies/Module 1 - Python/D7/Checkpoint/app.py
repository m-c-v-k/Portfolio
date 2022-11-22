#! python3

# Importing necessary libraries
from flask import *
import datetime
import psycopg2


def connect_db():
    """ Creates a connection to the database.

    Returns:
        object: Object containing the database connection.
    """

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="phonelist",
        user="postgres",
        password="MisoDaisy")

    return conn


def read_phonelist():
    """ Reeads all entries in the database.

    Returns:
        list: List of all entries in the database.
    """

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def read_phone(name):
    """ Selects the number from the database using the name associated with the name.

    Args:
        name (string): String containing the number of the person associated with the name.

    Returns:
        list: List containing the number associated with the entered name.
    """

    conn = connect_db()
    cur = conn.cursor()
    print(f"SELECT phone FROM phonelist WHERE name = '{name}';")
    cur.execute(f"SELECT phone FROM phonelist WHERE name = '{name}';")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def read_name(phone):
    """ Selects the name from the database using the name associated with the number.

    Args:
        name (string): String containing the name of the person associated with the number.

    Returns:
        list: List containing the name associated with the entered number.
    """

    conn = connect_db()
    cur = conn.cursor()
    print(f"SELECT name FROM phonelist WHERE phone = '{phone}';")
    cur.execute(f"SELECT name FROM phonelist WHERE phone = '{phone}';")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def add_phone(name, phone):
    """ Adds an entry in the database.

    Args:
        name (string): String containing the name for the new entry in the database.
        phone (string): String containing the phone number for the new entry in the database.

    Returns:
        string: String containing the name of the person added in the database.
    """

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

    return name


def delete_phone(name):
    """ Deletes an entry in the database.

    Args:
        name (string): String containing the name of the person to be deleted from the database.

    Returns:
        string: String containing the name of the person to be deleted from the database.
    """

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()

    return name


def get_date():
    """ Generates the current date in the format yy-mm-dd.

    Returns:
        string: String containing the current date.
    """
    now = datetime.datetime.now()
    today = [str(now.year % 100), str(now.month), str(now.day)]
    if len(today[1]) < 2:
        today[1] = '0'+today[1]
    if len(today[2]) < 2:
        today[2] = '0'+today[2]

    return today


app = Flask(__name__)

# Paths and their associated functions.


@app.route("/")
def start():
    """ Renders the start page: list.html
    Runs the function read_phonelist() to print the current phonelist.
    Runs the function get_date() to print the current date.

    Returns:
        string: Evaluation of the list.html file.
    """

    return render_template('list.html', list=read_phonelist(), date=get_date())


@app.route("/delete", methods=['POST', 'GET'])
def delete_func():
    """ Renders the delete page: delete.html
    Runs the delete_phone(name) to delete an entry in the database using data from the delete form.

    Returns:
        string: Evaluation of the delete.html file.
    """

    if request.method == 'POST':
        name = request.form['del_name']
        return render_template('delete.html', name=delete_phone(name))
    else:
        return render_template('list.html')


@app.route("/insert", methods=['POST', 'GET'])
def insert_func():
    """ Renders the insert page: indert.html
    Runs the add_phone(name, phone) to add an entry in the database using data from the insert form.

    Returns:
        string: Evaluation of the insert.html file.
    """

    if request.method == 'POST':
        name = request.form['inp_name']
        phone = request.form['inp_phone']
        return render_template('insert.html', name=add_phone(name, phone))
    else:
        return render_template('list.html')


@app.route("/api")
def api_func():
    """ Renders the api page: api_usage.html
    Gives the corresponding name or number to the supplied number or name using data from args.

    Runs the read_phone(name) to print the associated name.
    Runs the read_name(phone) to print the associated phone number.

    Returns:
        string: Evaluation of the api_usage.html file.
    """

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
    elif action == 'name':
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
    """ Renders the api_search page: api_search.html
    Lets the user search for a name or phone number and returns its associated value.

    Runs the read_phone(name) to print the associated name.
    Runs the read_name(phone) to print the associated phone number.

    Returns:
        string: Evaluation of the api_search.html file.
    """
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
        elif action == 'name':
            phone = inp
            if phone == "No number":
                return render_template('api_search.html', value="No number")
            name = read_name(phone)
            if len(name) <= 1:
                return render_template('api_search.html', value="Number not found")

            return render_template('api_search.html', value=name[0][0])
        else:
            return f"Unknown action: '{action}'"
