#! python3

# Import necessary libraries
import psycopg2


def select_from_location(conn, lat, lon):
    query = f"SELECT station_id FROM weather.location WHERE latitude = '{lat}' AND longitude = '{lon}';"
    value_id = ""
    print(lat)
    print(lon)

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute(query)

        # Check return from executed statement.
        row = cur.fetchone()

        if row == None:
            print("It seems as if there is no matching location.")
        else:
            value_id = row[0]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:

        cur.close()

        if value_id == "":
            value_id = None
        return value_id
