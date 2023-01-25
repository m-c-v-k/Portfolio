#! python3

# Import necessary libraries
import psycopg2


def select_from_forecast(conn, cols, lim):
    query = f"SELECT {cols} FROM weather.forecast WHERE {lim[0]} = '{lim[1]}' AND {lim[2]} = '{lim[3]}';"
    value_id = ""

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute(query)

        # Check return from executed statement.
        rows = cur.fetchall()

        if rows == []:
            print("It seems as if there is no matching location.")
        else:
            value_id = rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:

        cur.close()

        if value_id == "":
            value_id = None
        return value_id
