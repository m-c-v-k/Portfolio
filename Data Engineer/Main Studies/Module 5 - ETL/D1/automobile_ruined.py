#! python3

# Importing necessary libraries
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ruined_automobile_path = CURR_DIR_PATH + "/ruined_automobile_data-1.csv"

df = pd.read_csv(ruined_automobile_path)

is_analyzing = True

# Analyze functions (is_analyzing = True)


def analyze_rows():
    null_rows = df[df.isnull().any(axis=1)]
    print(null_rows)
    return null_rows


def analyze_nan_context(nan_df):
    for index, row in nan_df.iterrows():
        index = row['index']
        print(f"index: {index}")
        for n in range(index - 2, index + 3, 1):
            print(df[df['index'] == n])

        print("\n\n")


def analyze_duplicate_state():
    nan_fixed_path = CURR_DIR_PATH + "/nan_fixed_automobile.csv"
    df = pd.read_csv(nan_fixed_path)

    print("Duplicated rows")
    print(df[df.duplicated()])


def analyze_valid_entries():
    manufractures = [
        "alfa-romero", "audi", "bmw", "chevrolet",
        "dodge", "honda", "isuzu", "jaguar", "mazda",
        "mercedes-benz", "mitsubishi", "nissan", "porsche",
        "toyota", "volkswagen", "volvo"
    ]
    styles = [
        "convertible", "hatchback", "sedan", "wagon", "hardtop"
    ]

    dup_fixed_path = CURR_DIR_PATH + "/fixed_duplicated_automobile.csv"
    df = pd.read_csv(dup_fixed_path)

    manu_df = df['company']
    style_df = df['body-style']

    print(manu_df[~manu_df.isin(manufactures)])
    print(style_df[~style_df.isin(styles)])


def analyze_automobile():
    null_rows = analyze_rows()
    print(null_rows)
    analyze_nan_context(null_rows)
    analyze_duplicate_state()
    analyze_valid_entries()


# Repair functions (is_analyzing = False)


def repair_pad_nan():
    df.fillna(method="ffill", inplace=True)
    df.to_csv("nan_fixed_automobile.csv", index=False)


def repair_duplicated():
    nan_fixed_path = CURR_DIR_PATH + "/nan_fixed_automobile.csv"
    df = pd.read_csv(nan_fixed_path)

    df = df.drop_duplicates()
    df.to_csv("fixed_duplicated_automobile.csv", index=False)


def repair_invalid_manufacturer():
    dup_fixed_path = CURR_DIR_PATH + "/fixed_duplicated_automobile.csv"
    de = pd.read_csv(dup_fixed_path)

    df['company'] = df['company'].replace("alfa", value="alpha-romero")
    df.to_csv("fixed_automobile.csv", index=False)


def repair_data():
    repair_pad_nan()
    repair_duplicated()
    repair_invalid_manufacturer()


if is_analyzing:
    analyze_automobile()
else:
    repair_data()
