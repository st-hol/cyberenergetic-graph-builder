import math
import datetime
import random

import services.data_service as data_service
import services.tab1_service as tab1_service
import services.util_service as my_service


def get_usage_times(device):
    times = []
    cur_device_usage_time_list = device.usage_time_list
    for time in cur_device_usage_time_list:
        if time == "fulltime":
            times.append("fulltime")
            break
        date = datetime.datetime.strptime(str(time), '%Y-%mf-%d')
        #todo
