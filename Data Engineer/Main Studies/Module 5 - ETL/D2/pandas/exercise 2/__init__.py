#! python3

# Importing necessary libraries
import os
import glob
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def gather_subject_df(subject):
    data = []

    for file in glob.glob(f"{CURR_DIR_PATH}/data/raw/{subject}*"):
        subject_df = pd.read_csv(
            file,
            sep=',',
            encoding='unicode_escape'
        )
        data.append(subject_df)

    complete_df = pd.concat(data, axis=0)

    complete_df.to_csv(
        f"{CURR_DIR_PATH}/data/joined/{subject}_data.csv", index=False)

    return complete_df


def join_names(df, subject):

    if 'name' not in df.columns:
        name_column = df['firstname'] + " " + df['surname']
        df.insert(1, 'name', name_column)
        df.drop(['firstname', 'surname'], axis=1, inplace=True)

    df.to_csv(f"{CURR_DIR_PATH}/data/names/{subject}_data.csv", index=False)

    return df


def change_late(df, subject):

    if 'attendance' in df.columns:
        df['late'] = 60 - df['attendance']
    else:
        df['attendance'] = 60 - df['late']

    df.to_csv(f"{CURR_DIR_PATH}/data/late/{subject}_data.csv", index=False)

    return df


def check_late(all_df):
    complete_df = pd.concat(all_df)

    name_group = complete_df.groupby('name')
    absence_df = name_group[['name', 'late']].sum()
    absence_df = absence_df.sort_values(by='late', ascending=True)

    absence_df.to_csv(
        f"{CURR_DIR_PATH}/data/all_late/late_data.csv")

    return absence_df


biology_df = gather_subject_df('biology')
herbology_df = gather_subject_df('herbology')
math_df = gather_subject_df('math')
pe_df = gather_subject_df('pe')
physics_df = gather_subject_df('physics')

logy_df = join_names(biology_df, 'biology')
herbology_df = join_names(herbology_df, 'herbology')
math_df = join_names(math_df, 'math')
pe_df = join_names(pe_df, 'pe')
physics_df = join_names(physics_df, 'physics')

biology_df = change_late(biology_df, 'biology')
herbology_df = change_late(herbology_df, 'herbology')
math_df = change_late(math_df, 'math')
pe_df = change_late(pe_df, 'pe')
physics_df = change_late(physics_df, 'physics')

all_df = [logy_df, herbology_df, math_df, pe_df, physics_df]

late_df = check_late(all_df)
