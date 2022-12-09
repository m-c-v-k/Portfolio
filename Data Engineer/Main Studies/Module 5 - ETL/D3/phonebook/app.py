
import os
import sys
from flask import Flask, request
from flaskr.phonebook import Phonebook
from flaskr.mock_phonebook import initialize_mock

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append("..")

app = Flask(__name__)
phonebook = Phonebook(CURR_DIR_PATH + "/data/database.db")
initialize_mock(phonebook)


@app.route("/phonebook/")
def get_phonebook():
    return phonebook.get_all()


@app.route("/phonebook/name/<name_query>", methods=['GET', 'DELETE'])
def get_by_name(name_query):
    if request.method == 'GET':
        return phonebook.get_by_name(name_query)
    elif request.method == 'DELETE':
        return phonebook.delete_by_name(name_query)


@app.route("/phonebook", methods=["POST", "PUT"])
def enter_record():
    json_data = request.get_json()
    phonebook.add(json_data["entry"])
    return "Added to the phonebook", 201


@app.route("/phonebook/<num_of_rows>", methods=['GET'])
def get_phonebook_rows(num_of_rows):
    return phonebook.get_rows(num_of_rows)


@app.route("/phonebook/address/<address_query>")
def get_by_address(address_query):
    return phonebook.get_by_address(address_query)
