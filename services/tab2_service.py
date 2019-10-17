import math
import datetime
import random

import services.data_service as data_service
import services.util_service as my_service


def get_usage_times(device):
    times = []
    cur_device_usage_time_list = device.week_list
    for time in cur_device_usage_time_list:
        if time == "fulltime":
            times = data_service.time_range.copy()
            break
        parsed_time = datetime.datetime.strptime(str(time), '%H:%M')
        parsed_time = parsed_time.replace(
            year=datetime.date.today().year,
            month=datetime.date.today().month,
            day=datetime.date.today().day)
        times.append(parsed_time)
    return times


def intersected_map_of_device_usage(device):
    all_time = list(data_service.time_range)
    print(all_time)
    device_time = list(get_usage_times(device))
    print(device_time)
    intersected_map = dict.fromkeys(all_time, 0)
    for k, v in intersected_map.items():
        if k in device_time:
            intersected_map[k] = get_device_power_consumtion(device)
    return intersected_map


def get_device_power_consumtion(device):
    return device.consum_power
