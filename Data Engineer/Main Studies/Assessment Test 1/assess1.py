#! python3

# Importing necessary libraries
import psycopg2

### Functions ###


def connect_db():
    """ Connects to the database

    Returns:
        Object: Database connection
    """

    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="assessment",
            user="postgres",
            password="MisoDaisy"
        )

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def list_data(conn):
    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute("SELECT * FROM view_contacts;")

        # Check return from executed statement.
        rows = cur.fetchall()

        if rows is None:
            print("It seems as if there are no saved contacts.")
        else:
            print("Number of entries: " + str(cur.rowcount))
            for row in rows:
                print(f"{row[0]} {row[1]}, {row[2]}, {row[3]}, {row[4]}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close communication with databäase.
        cur.close()


def insert_data(conn):
    try:
        # Create a cursor.
        cur = conn.cursor()

        # Get relevant information
        contacts_first_name = input("Please input the first name").title()
        contacts_last_name = input("Please input the last name").title()
        contacts_title = input("Please input the title").title()
        contacts_organization = input("Please input the organization").title()

        if contacts_first_name == '':
            contacts_first_name = 'UNKNOWN'
        if contacts_last_name == '':
            contacts_last_name = 'NULL'
        if contacts_title == '':
            contacts_title = 'NULL'
        if contacts_organization == '':
            contacts_organization = 'NULL'

        # Executing statement.
        cur.execute(f"""INSERT INTO contacts (first_name, last_name, title, organization)
VALUES ('{contacts_first_name}', '{contacts_last_name}', '{contacts_title}', '{contacts_organization}');""")

        # Save table.
        save_changes(conn)

        items_numbers = int(
            input("Please input the number of contact informations to add"))

        # Find id
        cur.execute(
            f"SELECT id FROM contacts WHERE first_name = '{contacts_first_name}' AND last_name = '{contacts_last_name}';")
        # Check return from executed statement.
        rows = cur.fetchall()

        if rows is None:
            print("Can't find the contact.")
        else:
            for row in rows:
                contact_id = row[0]

        for entries in range(items_numbers):
            items_contact = input("Please input the contact information")
            items_type = input(
                "Please input the contact type (Email, Phone, Skype or Instagram)").title()
            items_category = input(
                "Please input the contact category (Home, Work, Fax)").title()

            if items_contact == '':
                items_contact = 'UNKNOWN'

            if items_type == '':
                items_type = 'NULL'
            elif items_type == 'Email':
                items_type = 1
            elif items_type == 'Phone':
                items_type = 2
            elif items_type == 'Skype':
                items_type = 3
            elif items_type == 'Instagram':
                items_type = 4

            if items_category == '':
                items_category = 'NULL'
            elif items_type == 'Home':
                items_type = 1
            elif items_type == 'Work':
                items_type = 2
            elif items_type == 'Fax':
                items_type = 3

            # Executing statement.
            cur.execute(f"""INSERT INTO items (contact, contact_id, contact_type_id, contact_category_id)
VALUES ('{items_contact}', '{contact_id}', '{items_type}', '{items_category}');""")

        print(f"{contacts_first_name} {contacts_last_name} added.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_changes(conn)

        # Close communication with database.
        cur.close()


def delete_data(conn, first_name, last_name):
    try:
        # Create a cursor:
        cur = conn.cursor()

        # Check if name in phonelist

        # Executing a statement.
        cur.execute("SELECT * FROM view_contacts;")

        # Check return from executed statement.
        rows = cur.fetchall()

        for row in rows:
            if first_name == row[0] and last_name == row[1]:
                # Executing statement.
                cur.execute(f"""DELETE FROM contacts
WHERE first_name = '{first_name}'
AND last_name = '{last_name}';""")
            print(f"{first_name} {last_name} deleted.")
        else:
            print("Name not recognized.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        save_changes(conn)

        # Close communication with database.
        cur.close()


def save_changes(conn):
    """ Commits changes to the database.

    Args:
        conn Object: Database connection
    """
    conn.commit()


# Running the program
conn = connect_db()

# Messages
print("Please enter one of the following commands:")
print("")
print("LIST - Prints a list of all contacts.")
print("INSERT - Inserts contact to list.")
print("DELETE first_name last_name - Deletes contact from list..")
print("QUIT - Exists the program.")

while True:
    user_input = input("Command: ").strip().split()

    user_input[0] = user_input[0].upper()

    # Formatting name
    first_name = user_input[1]
    first_name = name.title()
    last_name = user_input[2]
    last_name = name.title()

    # Selection menu
    # LIST
    if user_input[0] == "LIST":
        list_data(conn)

    # INSERT
    elif user_input[0] == "INSERT":
        insert_data(conn)

    # DELETE
    elif user_input[0] == "DELETE":
        delete_data(conn, first_name, last_name)

    # QUIT
    elif user_input[0] == "QUIT":
        print("Commiting all changes.")
        save_changes(conn)
        print("Connection to database closed.")
        print("Good bye!")
        break

    # Wrong input
    else:
        print("Please enter a valid command.")
        print("""LIST
LIST first_name last_name number
DELETE first_name last_name
QUIT""")
