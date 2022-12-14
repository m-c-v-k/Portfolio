#! python3

# Importing necessary libraries
import pandas as pd
import requests
import json
import os

# Get path
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# GET data from endpoint
r = requests.get('https://harvardartmuseums.org/browse')

# Print data from GET request
# TODO uncomment this print
# print(r.json())


### Extras ###

# Format the data
dict = r.json()
df_records = pd.DataFrame.from_records(dict['records'])

# Remove uninteresting columns
df_records = df_records.drop([
    'classificationid',
    'copyright',
    'contextualtextcount',
    'creditline',
    'accesslevel',
    'dateoflastpageview',
    'markscount',
    'publicationcount',
    'totaluniquepageviews',
    'contact',
    'colorcount',
    'verificationleveldescription',
    'state',
    'mediacount',
    'seeAlso',
    'rank',
    'period',
    'images',
    'objectid',
    'id',
    'imagecount',
    'exhibitioncount',
    'imagepermissionlevel',
    'techniqueid',
    'totalpageviews',
    'accessionyear',
    'standardreferencenumber',
    'labeltext',
    'worktypes',
    'signed',
    'relatedcount',
    'verificationlevel',
    'primaryimageurl',
    'titlescount',
    'peoplecount',
    'style',
    'lastupdate',
    'commentary',
    'periodid',
    'dateoffirstpageview',
    'century',
    'edition',
    'technique',
    'dimensions',
    'description',
    'medium',
    'division',
    'lendingpermissionlevel',
    'accessionmethod',
    'colors',
    'provenance',
    'groupcount',
    'datebegin',
    'url',
    'people',
    'department',
    'dateend'
], axis=1)

# Print the data
print(df_records.to_string())

# Save data to .json-file
df_records.to_json(f'{CURR_DIR_PATH}/records.json')
