import datetime
import math
import pandas as pd
import services.common_service as my_service

# North - Northeast - East - Southeast - South - Southwest - West - Northwest
# Север - Северо-Восток - Восток - Юго-Восток - Юг - Юго-Запад - Восток - Северо-Запад

compass_degree_map = {"Северный": 0,
                      "С-В": 45,
                      "Восточный": 90,
                      "Ю-В": 135,
                      "Южный": 180,
                      "Ю-З": 225,
                      "Западный": 270,
                      "С-З": 315,
                      "Переменный": 360}


def map_compass_to_degrees(wind_compass_names):
    wind_degrees = []
    for wd in wind_compass_names:
        degree = compass_degree_map.get(wd, 0)
        wind_degrees.append(degree)
    return wind_degrees


def map_speed_to_scale_one(wind_speed_list):
    max_speed = max(wind_speed_list)
    result = list(map(lambda x: float(x) / float(max_speed), wind_speed_list))
    return result


def map_temperature_frequency(all_data_map):
    distinct_temperatures = list(set(all_data_map["T"]))
    map_t_freq = dict.fromkeys(distinct_temperatures, 0)
    for t in all_data_map["T"]:
        map_t_freq[t] += 1
    map_t_freq = {k: map_t_freq[k] for k in map_t_freq if not math.isnan(k)}
    return map_t_freq


def map_full_datetime(all_data_map, path):
    days = my_service.restore_lost_data(all_data_map["days"])
    UTCs = my_service.restore_lost_data(all_data_map["UTC"])

    all_dates = []

    for day, utc in zip(days, UTCs):
        year = path[8:12]
        month = path[13:15]
        month = month.replace(".", "")
        day = datetime.datetime(year=int(year), month=int(month),
                                day=int(day), hour=utc.hour, minute=utc.minute)
        all_dates.append(day)
    return all_dates

# def map_full_datetime(all_data_map):
#     days = my_service.restore_lost_data(all_data_map["days"])
#     UTCs = my_service.restore_lost_data(all_data_map["UTC"])
#     months_in_year = 12
#     pattern = r'xlsdata/2012-{}.xlsx'
#     paths = [pattern.format(i + 1) for i in range(months_in_year)]
#
#     all_dates = []
#     for path in paths:
#         for day, utc in zip(days, UTCs):
#             year = path[8:12]
#             month = path[13:15]
#             month = month.replace(".", "")
#             day = datetime.datetime(year=int(year), month=int(month),
#                                     day=int(day), hour=utc.hour, minute=utc.minute)
#             all_dates.append(day)
#     return all_dates
