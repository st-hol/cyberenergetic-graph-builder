import math
import datetime
import random

import services.data_service as data_service
import services.util_service as my_service


kfc_y2 = 0.77


def get_usage_times(device):
    times = []
    cur_device_usage_time_list = device.week_list[data_service.get_tab2_day_of_week()]
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
    return W_all

def populate_p_max():
    W_all = sum_all_W_from_devices()
    return W_all


################################################

def get_all_devices_consumption_that_day():
    devices = data_service.get_electric_consumption_devices()

    all_time = list(data_service.time_range)
    all_cons_map = dict.fromkeys(all_time, 0)

    for device_name, device_entity in devices.items():
        # device_time = list(get_usage_times(device_name))
        intersected_map_of_usage = intersected_map_of_device_usage(device_entity)
        for t, Wt in intersected_map_of_usage.items():
            # if t in device_time:
            all_cons_map[t] += intersected_map_of_usage[t]
    # print("AALLLLLL", all_cons_map.values())
    return all_cons_map


def get_all_devices_sum_of_consumption_for_each_day():
    days_of_week = ["Mn","Tu","Wd","Th","Fr","Sa","Sn"]
    map_day_Wt = dict.fromkeys(days_of_week, 0)
    for day in days_of_week:
        data_service.set_tab2_day_of_week(day)
        all_cons_map = get_all_devices_consumption_that_day()
        sum_cons = sum(list(all_cons_map.values()))
        map_day_Wt[day] = sum_cons
    return map_day_Wt


