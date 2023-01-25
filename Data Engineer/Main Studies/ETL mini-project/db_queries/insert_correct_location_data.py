#! python3

# Import necessary libraries
import requests
import json
import os
import psycopg2
from connect_to_db import connect_to_db as connect
from location_data import location_data

# fill station data to database


def insert_data_to_location():
    conn = connect.connect_to_db()

    # Create a cursor.
    cur = conn.cursor()

    # Executing statement.
    nr = 0
    new_location_data = []
    for item in location_data:

        # Example test variables
        lat = item[1]
        lon = item[2]

        set_type = 'point'
        url_protocol = "https"
        url_domain = "opendata-download-metfcst.smhi.se"
        url_API = "api/category/pmp3g/version/2"
        url_type = f"geotype/{set_type}"
        url_point = f"lon/{lon}/lat/{lat}"
        url_data = "data.json"
        URL = f"{url_protocol}://{url_domain}/{url_API}/{url_type}/{url_point}/{url_data}"

        r = requests.get(URL)

        data = json.loads(r.text)
        coordinates = data['geometry']['coordinates'][0]
        coordinates = str(coordinates)
        coordinates = coordinates[1:-1]
        coordinates = coordinates.split(", ")

        temp_list = [item[0], coordinates[0], coordinates[1], item[3], item[4]]

        try:

            cur.execute(f""" INSERT INTO weather.location (station_id, latitude, longitude, name, active)
            VALUES
            ({temp_list[0]},
            '{temp_list[1]}',
            '{temp_list[2]}',
            '{temp_list[3]}',
            '{temp_list[4]}');
            """)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    conn.commit()

    # Close communication with database.
    cur.close()

    conn.close()


if __name__ == '__main__':
    insert_data_to_location()
