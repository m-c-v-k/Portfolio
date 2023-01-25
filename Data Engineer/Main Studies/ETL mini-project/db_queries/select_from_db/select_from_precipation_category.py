#! python3

# Import necessary libraries
import psycopg2


def select_from_precipation_category(conn, value):
    query = f"SELECT category_id FROM weather.precipitation_category WHERE meaning = '{value}';"
    value_id = ""

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute(query)

        # Check return from executed statement.
        row = cur.fetchone()

        if row == None:
            print("It seems as if there is no matching category.")
        else:
            value_id = row[0]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:

        cur.close()

        if value_id == "":
            value_id = None
        return value_id
