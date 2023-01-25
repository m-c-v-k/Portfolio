#! python3

# Import necessary libraries
import os
import glob
import datetime
import json
import psycopg2
from .connect_to_db import connect_to_db as connect
from .select_from_db import select_from_approved_time as sat
from .select_from_db import select_from_precipation_category as spc
from .select_from_db import select_from_location as sl
from .select_from_db import select_from_time as st


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OPEN_PATH = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def get_harmonized_data():
    os.chdir(OPEN_PATH)
    files_list = glob.glob('*.txt')
    data_file = max(files_list, key=os.path.getctime)

    with open(f'{OPEN_PATH}/{data_file}', 'r') as f:
        data = json.load(f)

    return data


def insert_to_db():
    data = get_harmonized_data()
    conn = connect.connect_to_db()

    approved_time_id = sat.select_from_approved_time(
        conn, data['approvedTime'], data['reference_time'])

    coordinates = data['location']
    coordinates = coordinates.split(", ")
    location_id = sl.select_from_location(
        conn, coordinates[0], coordinates[1])

    values_string = ""
    for i in range(len(data['valid_time'].split(', '))):
        temp_string = "("
        for key in data:
            if key == 'approvedTime':
                if data[key] == approved_time_id:
                    temp_string += f"'{data[key]}', "
            elif key == 'valid_time':
                values = data[key].split(', ')
                time_id = st.select_from_time(conn, values[i])
                if values[i] == time_id:
                    temp_string += f"'{values[i]}', "
            elif key == 'air_pressure':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'air_temperature':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'horizontal_visibility':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'wind_direction':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'wind_speed':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'relative_humidity':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'thunder_probability':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'mean_value_of_total_cloud_cover':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'mean_value_of_low_level_cloud_cover':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'mean_value_of_medium_level_cloud_cover':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'mean_value_of_high_level_cloud_cover':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'wind_gust_speed':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'minimum_precipitation_intensity':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'maximum_precipitation_intensity':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'percent_of_precipitation_in_frozen_form':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'precipitation_category':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'mean_precipitation_intensity':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'median_precipitation_intensity':
                values = data[key].split(', ')
                temp_string += values[i] + ', '
            elif key == 'location':
                temp_string += str(location_id) + ', '
            else:
                continue

        temp_string = temp_string[:-2]
        temp_string = temp_string + ')'
        values_string += temp_string + ', '

    values_string = values_string[:-2]

    column_string = """approved_time, location_id, valid_time, air_pressure, air_temperature, horizontal_visibility, wind_direction, wind_speed, relative_humidity, thunder_probability, mean_value_of_total_cloud_cover, mean_value_of_low_level_cloud_cover, mean_value_of_medium_level_cloud_cover, mean_value_of_high_level_cloud_cover, wind_gust_speed, minimum_precipitation_intensity, maximum_precipitation_intensity, percent_of_precipitation_in_frozen_form, precipitation_category, mean_precipitation_intensity, median_precipitation_intensity"""
    query = f"INSERT INTO weather.forecast ({column_string}) VALUES {values_string}"

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing statement.
        cur.execute(query)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        conn.commit()

        # Close communication with database.
        cur.close()

    conn.close()
