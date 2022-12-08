#! python3

# Importing necessary libraries
import os
import glob
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def gather_subject_df(subject):
    data = []

    for file in glob.glob(f"{CURR_DIR_PATH}/data/{subject}*"):
        subject_df = pd.read_csv(
            file,
            sep=',',
            encoding='unicode_escape'
        )
        data.append(subject_df)

    complete_df = pd.concat(data, axis=0)

    complete_df.to_csv(f"{CURR_DIR_PATH}/data/{subject}_data.csv", index=False)

    return complete_df


def join_names(df, subject):
    name_column = df['firstname'] + " " + df['surname']
    df.insert(1, 'name', name_column)
    df.drop(['firstname', 'surname'], axis=1, inplace=True)

    df.to_csv(f"{CURR_DIR_PATH}/data/{subject}_data.csv", index=False)

    return df


def check_late(df, subject):
    df.rename(columns={'attendence': 'late'}, inplace=True)

    df.to_csv(f"{CURR_DIR_PATH}/data/{subject}_data.csv", index=False)

    return df


biology_df = gather_subject_df('biology')
herbology_df = gather_subject_df('herbology')
math_df = gather_subject_df('math')
pe_df = gather_subject_df('pe')
physics_df = gather_subject_df('physics')

biology_df = join_names(biology_df, 'biology')
herbology_df = join_names(herbology_df, 'herbology')

biology_df = check_late(biology_df, 'biology')
herbology_df = check_late(herbology_df, 'herbology')
pe_df = check_late(pe_df, 'pe')
