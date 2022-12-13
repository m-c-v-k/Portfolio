from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash_operator import BashOperator

from random import randint
from datetime import *

import requests
import os
import configparser
import json

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def create_weather_string(lat, lon, appid):
    protocol = "https"
    domain = "api.openweathermap.org"
    API = "data/2.5/onecall"
    exclude = "exclude=minutely,alert"
    URL = f"{protocol}://{domain}/{API}?"
    URL += f"lat={lat}&lon={lon}&{exclude}&"
    URL += f"appid={appid}"

    return URL


def get_openweather(lat, lon, appid):
    URL = create_weather_string(lat, lon, appid)
    return requests.get(URL)


def write_weather_log():
    # Initialize configurations fron config.ini
    config = configparser.ConfigParser()
    config.read(CURR_DIR_PATH + "/../config.ini")

    # Fetch API_KEY from config.ini
    appid = config.get("DEV", "API_KEY")

    req = get_openweather(58.4, 15.6, appid)
    dict = json.loads(req.text)

    f = open(f"{CURR_DIR_PATH}/../data/weather.log", "w")
    for i in range(len(dict['hourly'])):
        hour = dict['hourly'][i]
        temp = hour['temp']-273.16
        humidity = hour['humidity']
        pressure = hour['pressure']
        f.write(f"{i},{temp},{humidity},{pressure}\n")
    f.close()


def _control_weather_file(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'read_weather'
    ])
    best_accuracy = max(accuracies)
    if not os.path.isfile('weather.log'):
        return 'read_failed'
    if os.stat('weather.log').st_size < 432:
        return 'read_failed'
    return 'read_OK'


def _read_weather():
    write_weather_log()
    return 10


with DAG("weather_dag", start_date=datetime(2021, 1, 1),
         schedule_interval=None, catchup=False) as dag:

    read_weather = PythonOperator(
        task_id="read_weather",
        python_callable=_read_weather
    )

    control_weather_file = BranchPythonOperator(
        task_id="control_weather_file",
        python_callable=_control_weather_file
    )

    read_OK = BashOperator(
        task_id="read_OK",
        bash_command="echo 'read_OK'"
    )

    read_failed = BashOperator(
        task_id="read_failed",
        bash_command="echo 'read_failed'"
    )

    [read_weather] >> control_weather_file >> [read_OK, read_failed]
