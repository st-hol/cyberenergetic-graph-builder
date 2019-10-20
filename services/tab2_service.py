import math
import datetime
import random

import services.data_service as data_service
import services.util_service as my_service


kfc_y2 = 0.77


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
    n_people = data_service.get_n_people()
    koef_optimized = 1
    if data_service.get_tab2_optimized():
        koef_optimized = data_service.get_koef_optimized()
    all_time = list(data_service.time_range)
    print(all_time)
    device_time = list(get_usage_times(device))
    print(device_time)
    intersected_map = dict.fromkeys(all_time, 0)
    for k, v in intersected_map.items():
        if k in device_time:
            intersected_map[k] = get_device_power_consumtion(device) * n_people * koef_optimized
    return intersected_map


def get_device_power_consumtion(device):
    return device.consum_power


#########################################


def calc_koef_optimized():
    P_ser = populate_p_ser()
    P_max = populate_p_max()
    k = float(P_ser/P_max)
    return k


def sum_all_W_from_devices():
    sum_all = 0
    for k, v in data_service.get_electric_consumption_devices().items():
        sum_all += v.consum_power
    return sum_all

def populate_p_ser():
    W_all = sum_all_W_from_devices() * math.fabs(float(kfc_y2))
    print("wwww--", W_all)
    return W_all

def populate_p_max():
    W_all = sum_all_W_from_devices()
    print("wwww-----------", W_all)
    return W_all

