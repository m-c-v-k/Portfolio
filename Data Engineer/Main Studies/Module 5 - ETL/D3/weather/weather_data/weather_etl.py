from glob import glob
import os
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_dir = CURR_DIR_PATH + "/data/"
target_dir = CURR_DIR_PATH + "/target/"

# This function extracts from multiple


def load_dfs_from(glob_path):
    subject_data = []
    # Gets a list of glob matches, ex. all csv files in target/late
    file_paths = glob(glob_path)

    for path in file_paths:
        df = pd.read_csv(path)
        # Appends a dataframe of stored data to the returned data
        subject_data.append(df)

    return subject_data, file_paths  # Returns extracted files paths and dataframes


def transform_weather():
    data, paths = load_dfs_from(f"{data_dir}*.csv")
    weather_data = []

    for path, entry in zip(paths, data):
        entry = entry.to_dict("records")[0]
        weather_entry = {
            "city": os.path.basename(path)[:-4],
            "tempature": entry["main.temp"] - 273,
            "weather": entry["weather.main"],
            "weather_desc": entry["weather.description"],
            "cloudy": entry["clouds.all"],
            "humid": entry["main.humidity"]
        }
        weather_data.append(weather_entry)

    df = pd.DataFrame(weather_data, columns=[
                      "city", "tempature", "weather", "weather_desc", "cloudy", "humid"])
    df.to_csv(target_dir + "final_weather.csv", index=False)
