#! python3

# Importing necessary libraries
import os
import pandas as pd
from functools import reduce

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def data_path(subject):
    return CURR_DIR_PATH + f"/data/{subject}*"


"""
complete_biology_df = reduce(lambda left, right: pd.merge(
    left, right, on=['subject']), biology_data)
"""


def gather_subject_df(subject):
    data = []

    for file in glob.glob(path):
        path = data_path(subject)
        subject_df = pd.read_csv(
            path,
            sep=',',
            encoding='unicode_escape'
        )
        data.append(subject_df)

    complete_df = pd.concat(data)

    complete_df.to_csv(f"{CURR_DIR_PATH}/data/{subject}_data.csv", index=False)

    return complete_df


biology_df = gather_subject_df('biology')
herbology_df = gather_subject_df('herbology')
math_df = gather_subject_df('math')
pe_df = gather_subject_df('pe')
physics_df = gather_subject_df('physics')
