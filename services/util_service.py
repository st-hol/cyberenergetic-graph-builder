import services.tab1_service as tab1_service
import services.common_service as my_service
import datetime
import pandas as pd
import numpy as np
import math
import numbers
import datetime
import os
import re


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%m/%d/%Y').date()


def parse_time(time_str):
    if time_str == '24:00':
        time_str = '00:00'
    return datetime.datetime.strptime(time_str, '%H:%M').time()


def flatten_list(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def map_full_datetime(all_data_map, path):
    days = restore_lost_data(all_data_map["days"])
    UTCs = restore_lost_data(all_data_map["UTC"])

    all_dates = []

    for day, utc in zip(days, UTCs):
        year = path[13:17]
        month = path[18:20]
        month = month.replace(".", "")
        day = datetime.datetime(year=int(year), month=int(month),
                                day=int(day), hour=utc.hour, minute=utc.minute)
        all_dates.append(day)
    return all_dates


def map_full_datetime_from_date_and_time(all_data_map):
    dates = restore_lost_data(all_data_map["date"])
    times = restore_lost_data(all_data_map["time"])

    all_dates = []
    for date_str, time_str in zip(dates, times):
        date_object = parse_date(date_str)
        time_object = parse_time(time_str)
        day = datetime.datetime(year=int(date_object.year), month=int(date_object.month),
                                day=int(date_object.day), hour=time_object.hour, minute=time_object.minute)
        all_dates.append(day)

    return all_dates



def check_is_nan(x):
    if isinstance(x, datetime.datetime):
        return False
    if isinstance(x, numbers.Number):
        return math.isnan(x)
    if isinstance(x, str):
        return x == ""




def check_is_nan_for_muni(x):
    if isinstance(x, datetime.datetime):
        return False
    if isinstance(x, numbers.Number):
        return math.isnan(x) or x == 0
    if isinstance(x, str):
        return x == "" or x == "0"


def restore_lost_data_for_muni(l):
    restored = l.copy()
    if all(check_is_nan_for_muni(v) is True for v in l):
        restored = [0 for i in l]
        return restored
    else:
        for i in range(len(l)):
            if check_is_nan_for_muni(l[i]):
                restored[i] = interpolate_for_muni(l, i)
        return restored


def restore_lost_data(l):
    restored = l.copy()
    if all(check_is_nan(v) is True for v in l):
        restored = [0 for i in l]
        return restored
    else:
        for i in range(len(l)):
            if check_is_nan(l[i]):
                restored[i] = interpolate(l, i)
        return restored


def interpolate(l, index):
    middle_ind = int(len(l) / 2)
    if index > middle_ind:
        return_value = l[len(l) - 1]
        i = middle_ind
        while i < len(l):
            if check_is_nan(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    else:
        return_value = l[0]
        i = 0
        while i < middle_ind:
            if check_is_nan(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    return return_value


def interpolate_for_muni(l, index):
    middle_ind = int(len(l) / 2)
    if index > middle_ind:
        return_value = l[len(l) - 1]
        i = middle_ind
        while i < len(l):
            if check_is_nan_for_muni(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    else:
        return_value = l[0]
        i = 0
        while i < middle_ind:
            if check_is_nan_for_muni(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    return return_value


def map_to_logarithmic(l):
    result = list(map(lambda x: float(math.log(x)), l))
    return result



