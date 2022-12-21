#! python3

# Importing necessary libraries
import pandas as pd
import requests
import os
import io

# Creating path variable
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# 5.1


def csv_to_json(file):
    """ Converts any .csv-file to a .json-file

    Args:
        file (string): File name as a string, not including the file extention.
    """
    file_name = file + '_json'

    df = pd.read_csv(f'{CURR_DIR_PATH}/{file}.csv')
    df.to_json(f'{CURR_DIR_PATH}/{file_name}.json')


csv_to_json('doggie')

# 5.2


def wiki_to_json(article):
    """ Takes any English Wikipedia-article and saves it to a .json-file

    Args:
        article (string): Article name as represented in the browser search-bar.
    """
    article = article.lower()
    protocol = 'https'
    website = 'en.wikipedia.org'
    api_loc = 'w/api.php'
    query = f'?action=query&exlimit=1&explaintext=1&exsectionformat=plain&prop=extracts&titles={article}&format=json'

    api_path = f'{protocol}://{website}/{api_loc}{query}'

    file_name = article + '_json'

    r = requests.get(api_path).content

    df = pd.read_json(io.StringIO(r.decode('utf-8')))

    df.to_json(f'{CURR_DIR_PATH}/{file_name}.json')


wiki_to_json('Italian_cuisine')
