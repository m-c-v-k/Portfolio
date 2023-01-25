#! python3

# Import necessary libraries
import os
import psycopg2
import configparser

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = f'{CURR_DIR_PATH}/db_access/config.ini'


def connect_to_db():
    conn = None

    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        print("Connecting to database...")
        conn = psycopg2.connect(
            host=config['database']['HOST'],
            port=config['database']['PORT'],
            database=config['database']['DATABASE'],
            user=config['database']['USER'],
            password=config['database']['PASSWORD']
        )

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn
