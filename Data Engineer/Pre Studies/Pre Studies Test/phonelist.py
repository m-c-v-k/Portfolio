#! Python3

"""
Construct a Python program with a text interface that reads and write to a phone list 
database in PostgreSQL. 

In this program there shall be four commands, list, add, delete, and quit: 

LIST lists all phone numbers in the table 
ADD adds a person and a phone number to the phone list 
DELETE deletes a person from the phone list 
QUIT quits the program and saves unsaved changes
"""

# Importing necessary libraries
import psycopg2


def read_phonelist(conn):
    """ Reads all entries in the phonelist.

    Args:
        conn (class): psycopg2.extensions.connection connects to database.
    """

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute("SELECT * FROM phonelist;")

        # Check return from executed statement.
        rows = cur.fetchall()

        if rows is None:
            print("It seems as if there are no saved numbers.")
        else:
            print("Number of entries: " + str(cur.rowcount))
            for row in rows:
                print(f"{row[0]}:    {row[1]}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close communication with databäase.
        cur.close()


def add_phone(conn, name, phone):
    """ Adds an entry to the phonelist.

    Args:
        conn (class): psycopg2.extensions.connection connects to database.
        name (string): String containing name to be entered.
        phone (string): String containing phone number to be entered.
    """

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing statement.
        cur.execute(f"""INSERT INTO phonelist (name, phone)
VALUES ('{name}', '{phone}');""")
        print(f"{name} added.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_phonelist(conn)

        # Close communication with database.
        cur.close()


def delete_phone(conn, name):
    """ Deletes entry in the phonelist.

    Args:
        conn (class): psycopg2.extensions.connection connects to database.
        name (string): String containing name to be deleted.
    """

    try:
        # Create a cursor:
        cur = conn.cursor()

        # Check if name in phonelist

        # Executing a statement.
        cur.execute("SELECT * FROM phonelist;")

        # Check return from executed statement.
        rows = cur.fetchall()

        for row in rows:
            if name in row:
                # Executing statement.
                cur.execute(f"""DELETE FROM phonelist
WHERE name = '{name}';""")
            print(f"{name} deleted.")
        else:
            print("Name not recognized.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_phonelist(conn)

        # Close communication with database.
        cur.close()


def save_phonelist(conn):
    """ Saves changes to database.

    Args:
        conn (class): psycopg2.extensions.connection connects to database.
    """

    # committing changes to table.
    conn.commit()


def phonebook():
    """ Main function for handling everything regarding the phonelist
    """

    conn = None

    try:
        # Connect to db
        print("Connecting to database...")
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="phonedb",
            user="postgres",
            password="MisoDaisy"
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Messages
    print("Please enter one of the following commands:")
    print("")
    print("LIST - Prints a list of all contacts and numbers.")
    print("ADD fist_name last_name number - Adds contact to list.")
    print("DELETE first_name last_name - Deletes contact from list.")
    print("QUIT - Exists the program.")

    # Control loop
    while True:

        # Handle input
        usr_inp = input("Command: ").strip().split()

        usr_inp[0] = usr_inp[0].upper()

        # Formatting name
        name = " ".join(usr_inp[1:3])
        name = name.title()

        # Selection menu
        # LIST
        if usr_inp[0] == "LIST":
            read_phonelist(conn)

        # ADD
        elif usr_inp[0] == "ADD":
            add_phone(conn, name, usr_inp[3])

        # DELETE
        elif usr_inp[0] == "DELETE":
            delete_phone(conn, name)

        # QUIT
        elif usr_inp[0] == "QUIT":
            print("Commiting all changes.")
            save_phonelist(conn)
            conn.close()
            print("Connection to database closed.")
            print("Good bye!")
            break

        # Wrong input
        else:
            print("Please enter a valid command.")
            print("""LIST
ADD first_name last_name number
DELETE first_name last_name
QUIT""")


# Run function
phonebook()
