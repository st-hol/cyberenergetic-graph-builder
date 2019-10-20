import pandas as pd
import numpy as np
import math
import numbers
import datetime
import os
import re

import services.tab2_service as tab2_service
import services.util_service as util_service


def read_csv_with_interval(report_city="kyiv"):
    start_date_muni = get_start_date_muni()
    end_date_muni = get_end_date_muni()
    cut_bank_muni_ap_map = read_csv(report_city)

    try:
        start_index = np.where(cut_bank_muni_ap_map["date"] == start_date_muni)
        if start_index[0].size == 0:
            raise ValueError
    except ValueError:
        start_index = list()
        start_index.append([0])

    try:
        end_index = np.where(cut_bank_muni_ap_map["date"] == end_date_muni)
        if end_index[0].size == 0:
            raise ValueError
    except ValueError:
        end_index = list()
        end_index.append([-1])

    start_index = start_index[0][0]
    end_index = end_index[0][0]

    cut_bank_muni_ap_map["date"] = cut_bank_muni_ap_map["date"][start_index:end_index]
    cut_bank_muni_ap_map["time"] = cut_bank_muni_ap_map["time"][start_index:end_index]
    cut_bank_muni_ap_map["etrn"] = cut_bank_muni_ap_map["etrn"][start_index:end_index]
    cut_bank_muni_ap_map["fullDate"] = util_service.map_full_datetime_from_date_and_time(cut_bank_muni_ap_map)

    return cut_bank_muni_ap_map


# Date (MM/DD/YYYY),Time (HH:MM),ETR (W/m^2),ETRN (W/m^2),GHI (W/m^2),GHI source,GHI uncert (%),DNI (W/m^2),DNI source,DNI uncert (%),DHI (W/m^2),DHI source,DHI uncert (%),GH illum (lx),GH illum source,Global illum uncert (%),DN illum (lx),DN illum source,DN illum uncert (%),DH illum (lx),DH illum source,DH illum uncert (%),Zenith lum (cd/m^2),Zenith lum source,Zenith lum uncert (%),TotCld (tenths),TotCld source,TotCld uncert (code),OpqCld (tenths),OpqCld source,OpqCld uncert (code),Dry-bulb (C),Dry-bulb source,Dry-bulb uncert (code),Dew-point (C),Dew-point source,Dew-point uncert (code),RHum (%),RHum source,RHum uncert (code),Pressure (mbar),Pressure source,Pressure uncert (code),Wdir (degrees),Wdir source,Wdir uncert (code),Wspd (m/s),Wspd source,Wspd uncert (code),Hvis (m),Hvis source,Hvis uncert (code),CeilHgt (m),CeilHgt source,CeilHgt uncert (code),Pwat (cm),Pwat source,Pwat uncert (code),AOD (unitless),AOD source,AOD uncert (code),Alb (unitless),Alb source,Alb uncert (code),Lprecip depth (mm),Lprecip quantity (hr),Lprecip source,Lprecip uncert (code)
def read_csv(report_city="kyiv"):
    cut_bank_muni_ap_map = {}
    path = r'xlsdata/' + report_city + '-data.csv'
    data = pd.read_csv(path)

    dates = data['Date (MM/DD/YYYY)']
    times = data['Time (HH:MM)']
    etrn = data['ETRN (W/m^2)']

    cut_bank_muni_ap_map["date"] = dates.values
    cut_bank_muni_ap_map["time"] = times.values
    cut_bank_muni_ap_map["etrn"] = etrn.values

    cut_bank_muni_ap_map["fullDate"] = util_service.map_full_datetime_from_date_and_time(cut_bank_muni_ap_map)
    return cut_bank_muni_ap_map


def read_xml_all_months_with_interval(start, end):
    # start_date = get_start_date()
    # end_date = get_end_date()
    start_date = start
    end_date = end
    all_data_map = read_xml_all_months()

    if start_date != "UNDEFINED" and end_date != "UNDEFINED":
        start_date = datetime.datetime.strptime(str(start_date), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d')

    print(start_date)
    # print(all_data_map["fullDate"][0])
    print(end_date)
    try:
        start_index = all_data_map["fullDate"].index(start_date)
    except ValueError:
        start_index = 0

    try:
        end_index = all_data_map["fullDate"].index(end_date)
    except ValueError:
        end_index = -1

    print(start_index)
    print(end_index)

    all_data_map["days"] = all_data_map["days"][start_index:end_index]
    all_data_map["UTC"] = all_data_map["UTC"][start_index:end_index]
    all_data_map["T"] = all_data_map["T"][start_index:end_index]
    all_data_map["dd"] = all_data_map["dd"][start_index:end_index]
    all_data_map["FF"] = all_data_map["FF"][start_index:end_index]
    # all_data_map["ww"].extend(all_data_map["ww"])
    # all_data_map["N"].extend(all_data_map["N"])
    # all_data_map["vv"].extend(all_data_map["vv"])
    # all_data_map["U"].extend(all_data_map["U"])
    # all_data_map["PPP"].extend(all_data_map["PPP"])
    # all_data_map["hhh"].extend(all_data_map["hhh"])
    all_data_map["fullDate"] = all_data_map["fullDate"][start_index:end_index]

    return all_data_map


def read_xml_from_single_report(path):
    all_data_map = {}
    data = pd.read_excel(path)
    days_of_month = pd.DataFrame(data, columns=['Число месяца'])
    UTC = pd.DataFrame(data, columns=['UTC'])
    T = pd.DataFrame(data, columns=['T'])
    dd = pd.DataFrame(data, columns=['dd'])
    FF = pd.DataFrame(data, columns=['FF'])
    # ww = pd.DataFrame(data, columns=['ww'])
    # N = pd.DataFrame(data, columns=['N'])
    # vv = pd.DataFrame(data, columns=['vv'])
    # U = pd.DataFrame(data, columns=['U'])
    # PPP = pd.DataFrame(data, columns=['PPP'])
    # hhh = pd.DataFrame(data, columns=['hhh'])
    all_data_map["days"] = util_service.flatten_list(days_of_month.values)
    all_data_map["UTC"] = util_service.flatten_list(UTC.values)
    all_data_map["T"] = util_service.flatten_list(T.values)
    all_data_map["dd"] = util_service.flatten_list(dd.values)
    all_data_map["FF"] = util_service.flatten_list(FF.values)
    # all_data_map["ww"] = flatten_list(ww.values)
    # all_data_map["N"] = flatten_list(N.values)
    # all_data_map["vv"] = flatten_list(vv.values)
    # all_data_map["U"] = flatten_list(U.values)
    # all_data_map["PPP"] = flatten_list(PPP.values)
    # all_data_map["hhh"] = flatten_list(hhh.values)

    all_data_map["fullDate"] = util_service.map_full_datetime(all_data_map, path)

    return all_data_map


def obtain_xls_files_from_directory():
    dir_name = r'xlsdata/'
    paths = [dir_name + name for name in os.listdir(dir_name)
             if os.path.isfile(os.path.join(dir_name, name))
             and re.match(r'(\D)+-(\d)+-(\d)+\.xlsx', name)
             and not name.startswith('~')]
    paths.sort(key=len)
    return paths


# months_in_year = 12
def read_xml_all_months():
    paths = obtain_xls_files_from_directory()
    n_of_files = len(paths)
    print("Number of Files using listdir method#2 :", n_of_files)
    print(paths)

    all_data_from_all_reports = dict()
    all_data_from_all_reports["days"] = []
    all_data_from_all_reports["UTC"] = []
    all_data_from_all_reports["T"] = []
    all_data_from_all_reports["dd"] = []
    all_data_from_all_reports["FF"] = []
    # all_data_from_all_reports["ww"] = []
    # all_data_from_all_reports["N"] = []
    # all_data_from_all_reports["vv"] = []
    # all_data_from_all_reports["U"] = []
    # all_data_from_all_reports["PPP"] = []
    # all_data_from_all_reports["hhh"] = []
    all_data_from_all_reports["fullDate"] = []

    for p in paths:
        all_data_from_current_report = read_xml_from_single_report(p)

        all_data_from_all_reports["days"].extend(all_data_from_current_report["days"])
        all_data_from_all_reports["UTC"].extend(all_data_from_current_report["UTC"])
        all_data_from_all_reports["T"].extend(all_data_from_current_report["T"])
        all_data_from_all_reports["dd"].extend(all_data_from_current_report["dd"])
        all_data_from_all_reports["FF"].extend(all_data_from_current_report["FF"])
        # all_data_from_all_reports["ww"].extend(all_data_from_current_report["ww"])
        # all_data_from_all_reports["N"].extend(all_data_from_current_report["N"])
        # all_data_from_all_reports["vv"].extend(all_data_from_current_report["vv"])
        # all_data_from_all_reports["U"].extend(all_data_from_current_report["U"])
        # all_data_from_all_reports["PPP"].extend(all_data_from_current_report["PPP"])
        # all_data_from_all_reports["hhh"].extend(all_data_from_current_report["hhh"])
        all_data_from_all_reports["fullDate"].extend(all_data_from_current_report["fullDate"])

    return all_data_from_all_reports


start_date = 'UNDEFINED'
end_date = 'UNDEFINED'


def get_start_date():
    global start_date
    return start_date


def get_end_date():
    global end_date
    return end_date


start_date_muni = 'UNDEFINED'
end_date_muni = 'UNDEFINED'


def get_start_date_muni():
    global start_date_muni
    return start_date_muni


def get_end_date_muni():
    global end_date_muni
    return end_date_muni


is_active = "NO_ONE_IS_ACTIVE_NOW"
all_data_map = read_xml_all_months_with_interval(
    get_start_date(), get_end_date()
)
cut_bank_muni_ap_map = read_csv_with_interval()


# data
def update_all_data_map(start, end):
    global all_data_map
    all_data_map = read_xml_all_months_with_interval(start, end)


def update_cut_bank_muni_ap_map():
    global cut_bank_muni_ap_map
    cut_bank_muni_ap_map = read_csv_with_interval()


def get_all_data_map():
    global all_data_map
    return all_data_map


# def set_all_data_map(m):
#     global all_data_map
#     all_data_map = m
def get_cut_bank_muni_ap_map():
    global cut_bank_muni_ap_map
    return cut_bank_muni_ap_map


# def set_cut_bank_muni_ap_map(m):
#     global cut_bank_muni_ap_map
#     cut_bank_muni_ap_map = m


def get_active():
    global is_active
    return is_active


def set_active(s):
    global is_active
    is_active = s


def display_graph_and_set_active(controller, frame, active):
    global is_active
    is_active = active
    print("log: is active (graph) : ", is_active)
    controller.show_frame(frame)


def set_date_interval(start, end):
    global start_date
    global end_date
    start_date = start
    end_date = end
    print(start_date)
    print(end_date)


def set_date_muni_interval(start, end):
    global start_date_muni
    global end_date_muni
    start_date_muni = start
    end_date_muni = end
    print(start_date_muni)
    print(end_date_muni)


def get_date_interval():
    global start_date
    global end_date
    return [start_date, end_date]


def get_date_muni_interval():
    global start_date_muni
    global end_date_muni
    return [start_date_muni, end_date_muni]


n_people = 1


def get_n_people():
    global n_people
    return n_people


def set_n_people(s):
    global n_people
    n_people = int(s)
    print(n_people)


S = 42


def get_S():
    global S
    return S


def set_S(s):
    global S
    S = float(s)
    print(S)


n_vann = 1


def get_n_vann():
    global n_vann
    return n_vann


def set_n_vann(s):
    global n_vann
    n_vann = int(s)
    print(n_vann)


n_dush = 1


def get_n_dush():
    global n_dush
    return n_dush


def set_n_dush(s):
    global n_dush
    n_dush = int(s)
    print(n_dush)


temperature_desired = 20


def get_temperature_desired():
    global temperature_desired
    return temperature_desired


def set_temperature_desired(s):
    global temperature_desired
    temperature_desired = float(s)
    print(temperature_desired)


# опалювальный по умолч.
# start_date_tab3 = "2012-01-01"
# end_date_tab3 = "2012-03-01"

start_date_tab3 = "UNDEFINED"
end_date_tab3 = "UNDEFINED"


def set_date_tab3_interval(start, end):
    global start_date_tab3
    global end_date_tab3
    start_date_tab3 = start
    end_date_tab3 = end
    print(start_date_tab3)
    print(end_date_tab3)


def get_date_tab3_interval():
    global start_date_tab3
    global end_date_tab3
    return [start_date_tab3, end_date_tab3]


def set_tab3_data(n_people, s, n_dush, n_vann, t_desired, startdate, enddate):
    set_active("3_1")
    set_n_people(n_people)
    set_S(s)
    set_n_dush(n_dush)
    set_n_vann(n_vann)
    set_temperature_desired(t_desired)
    set_date_tab3_interval(startdate, enddate)


#################  tab 2 #################

class EnergyConsumptionDevice:
    def __init__(self, consum_power, week_list, quantity):
        self.consum_power = consum_power
        self.week_list = week_list
        self.quantity = quantity


time_range = np.array([datetime.datetime(datetime.date.today().year,
                                         datetime.date.today().month,
                                         datetime.date.today().day,
                                         i, 0) for i in range(24)])

electric_consumption_devices = dict()
electric_consumption_devices['fridge'] = EnergyConsumptionDevice(0.3 * 10 ** 3, ["fulltime"], 1)
electric_consumption_devices['cooker'] = EnergyConsumptionDevice(3.5 * 10 ** 3, ["8:00", "14:00", "18:00"], 1)
electric_consumption_devices['microwave'] = EnergyConsumptionDevice(2.2 * 10 ** 3, ["11:00", "16:00"], 1)
electric_consumption_devices['teapot'] = EnergyConsumptionDevice(2 * 10 ** 3,
                                                               ["9:00", "12:00", "14:00", "17:00", "19:0"], 1)
electric_consumption_devices['computer'] = EnergyConsumptionDevice(0.25 * 10 ** 3, ["19:00", "20:00", "21:00", "22:00"],
                                                                   1)

def get_electric_consumption_devices():
    global electric_consumption_devices
    print("DEVICES:", electric_consumption_devices)
    return electric_consumption_devices


tab2_optimized = True


def get_tab2_optimized():
    global tab2_optimized
    return tab2_optimized


def set_tab2_optimized(s):
    global tab2_optimized
    if s == "+":
        tab2_optimized = True
    else:
        tab2_optimized = False


koef_optimized = 1
def get_koef_optimized():
    global koef_optimized
    if get_tab2_optimized():
        koef_optimized = tab2_service.calc_koef_optimized()
    else:
        koef_optimized = 1
    return koef_optimized


def set_tab2_data(n_people, is_optimized):
    set_n_people(n_people)
    set_tab2_optimized(is_optimized)


