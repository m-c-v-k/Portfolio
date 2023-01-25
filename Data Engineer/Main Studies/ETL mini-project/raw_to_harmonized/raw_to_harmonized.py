#! python3

# Import necessary libraries
import os
import glob
import datetime
import datetime
import json

# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OPEN_PATH = f'{CURR_DIR_PATH}/../data/testing/raw'
SAVE_PATH = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def get_raw_Data():
    os.chdir(OPEN_PATH)
    files_list = glob.glob('*.json')
    data_file = max(files_list, key=os.path.getctime)

    with open(f'{OPEN_PATH}/{data_file}', 'r') as f:
        data = json.load(f)

    return data, data_file


def handle_time(time):
    time = datetime.datetime.strptime(
        time, '%Y-%M-%dT%H:%S:%fZ')
    time = datetime.datetime.strftime(
        time, '%Y-%M-%d %H:%M:%S')

    return time


def harmonizing_data(data):
    # Harmonized dictionary
    data_dict = {}

    # Forecast data
    valid_time_value = ""
    spp_value = ""
    pcat_value = ""
    pmin_value = ""
    pmean_value = ""
    pmax_value = ""
    pmedian_value = ""
    tcc_mean_value = ""
    lcc_mean_value = ""
    mcc_mean_value = ""
    hcc_mean_value = ""
    t_value = ""
    msl_value = ""
    vis_value = ""
    wd_value = ""
    ws_value = ""
    r_value = ""
    tstm_value = ""
    gust_value = ""

    for validTime in data['timeSeries']:
        valid_time_value += f"{handle_time(validTime['validTime'])}, "
        for parameters in validTime['parameters']:
            if parameters['name'] == "spp":
                spp_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "pmin":
                pmin_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "pmean":
                pmean_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "pmax":
                pmax_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "pmedian":
                pmedian_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "tcc_mean":
                tcc_mean_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "lcc_mean":
                lcc_mean_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "mcc_mean":
                mcc_mean_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "hcc_mean":
                hcc_mean_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "t":
                t_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "msl":
                msl_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "vis":
                vis_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "wd":
                wd_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "ws":
                ws_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "r":
                r_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "tstm":
                tstm_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "gust":
                gust_value += f"{str(parameters['values'][0])}, "
            elif parameters['name'] == "pcat":
                pcat_value += f"{str(parameters['values'][0])}, "

    data_dict['approvedTime'] = handle_time(data['approvedTime'])
    data_dict['reference_time'] = handle_time(data['referenceTime'])
    data_dict['location'] = str(data['geometry']['coordinates'])[2:-2]
    data_dict['valid_time'] = valid_time_value[:-2]
    data_dict['air_pressure'] = msl_value[:-2]
    data_dict['air_temperature'] = t_value[:-2]
    data_dict['horizontal_visibility'] = vis_value[:-2]
    data_dict['wind_direction'] = wd_value[:-2]
    data_dict['wind_speed'] = ws_value[:-2]
    data_dict['relative_humidity'] = r_value[:-2]
    data_dict['thunder_probability'] = tstm_value[:-2]
    data_dict['mean_value_of_total_cloud_cover'] = tcc_mean_value[:-2]
    data_dict['mean_value_of_low_level_cloud_cover'] = lcc_mean_value[:-2]
    data_dict['mean_value_of_medium_level_cloud_cover'] = mcc_mean_value[:-2]
    data_dict['mean_value_of_high_level_cloud_cover'] = hcc_mean_value[:-2]
    data_dict['wind_gust_speed'] = gust_value[:-2]
    data_dict['minimum_precipitation_intensity'] = pmin_value[:-2]
    data_dict['maximum_precipitation_intensity'] = pmax_value[:-2]
    data_dict['percent_of_precipitation_in_frozen_form'] = spp_value[:-2]
    data_dict['precipitation_category'] = pcat_value[:-2]
    data_dict['mean_precipitation_intensity'] = pmean_value[:-2]
    data_dict['median_precipitation_intensity'] = pmedian_value[:-2]

    return data_dict


def save_harmonized_data(lat, lon):
    data, file_name = get_raw_Data()
    file_name = f'harmonized_data_{lat}_{lon}_{file_name[-18:-5]}'

    data = harmonizing_data(data)

    with open(f'{SAVE_PATH}/{file_name}.txt', 'w+') as f:
        json.dump(data, f)
