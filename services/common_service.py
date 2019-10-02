import pandas as pd
import numpy as np
import math
import numbers
import datetime
import os
import re

import services.tab1_service as tab1_service

start_date = 'UNDEFINED'
end_date = 'UNDEFINED'
start_date_muni = 'UNDEFINED'
end_date_muni = 'UNDEFINED'


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


def read_csv_with_interval(report_city="kyiv"):
    global start_date_muni
    global end_date_muni
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
    cut_bank_muni_ap_map["fullDate"] = tab1_service.map_full_datetime_from_date_and_time(cut_bank_muni_ap_map)

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

    cut_bank_muni_ap_map["fullDate"] = tab1_service.map_full_datetime_from_date_and_time(cut_bank_muni_ap_map)
    return cut_bank_muni_ap_map


def read_xml_all_months_with_interval():
    global start_date
    global end_date
    all_data_map = read_xml_all_months()

    if start_date != "UNDEFINED" and end_date != "UNDEFINED":
        start_date = datetime.datetime.strptime(str(start_date), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d')

    print(start_date)
    print(all_data_map["fullDate"][0])
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
    all_data_map["days"] = flatten_list(days_of_month.values)
    all_data_map["UTC"] = flatten_list(UTC.values)
    all_data_map["T"] = flatten_list(T.values)
    all_data_map["dd"] = flatten_list(dd.values)
    all_data_map["FF"] = flatten_list(FF.values)
    # all_data_map["ww"] = flatten_list(ww.values)
    # all_data_map["N"] = flatten_list(N.values)
    # all_data_map["vv"] = flatten_list(vv.values)
    # all_data_map["U"] = flatten_list(U.values)
    # all_data_map["PPP"] = flatten_list(PPP.values)
    # all_data_map["hhh"] = flatten_list(hhh.values)

    all_data_map["fullDate"] = tab1_service.map_full_datetime(all_data_map, path)

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


def check_is_nan(x):
    if isinstance(x, datetime.datetime):
        return False
    if isinstance(x, numbers.Number):
        return math.isnan(x)
    if isinstance(x, str):
        return x == ""


def flatten_list(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list


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




























# pattern = dir_name + report_city + "-" + report_year + '-{}.xlsx'
# paths = [pattern.format(i + 1) for i in range(n_of_files)]

# def read_by_lines():
#     filename = r'xlsdata/data.txt'
#     with open(filename) as f:
#         content = f.readlines()
#
#     content = [x.strip() for x in content]
#     #  [print(x) for x in content]
#     maped_content = [[col.split(",") for col in row] for row in content]
#     [[print(col) for col in row] for row in maped_content]


# def extend_with_full_date(all_data_map, path):
#     all_data_map["fullDate"] = []
#     for day, utc in zip(all_data_map["days"], all_data_map["UTC"]):
#         year = path[8:12]
#         month = path[13:15]
#         month = month.replace(".", "")
#         day = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=utc.hour, minute=utc.minute)
#         all_data_map["fullDate"].append(day)


# print(read_xml_from_single_report()["hhh"])
# restored = restore_lost_data(read_xml_from_single_report()["hhh"])
# print(restored)
#
# r = restore_lost_data(read_xml_from_single_report()["U"])
# print(r)
# read_xml_from_single_report()


# names = ['Date (MM/DD/YYYY)', 'Time (HH:MM)', 'ETR (W/m^2)', 'ETRN (W/m^2)', 'GHI (W/m^2)',
#          'GHI source', 'GHI uncert (%)', 'DNI (W/m^2)', 'DNI source', 'DNI uncert (%)',
#          'DHI (W/m^2)', 'DHI source,DHI uncert (%)', 'GH illum (lx)', 'GH illum source',
#          'Global illum uncert (%)', 'DN illum (lx)', 'DN illum source', 'DN illum uncert (%)',
#          'DH illum (lx)', 'DH illum source', 'DH illum uncert (%)', 'Zenith lum (cd/m^2)',
#          'Zenith lum source', 'Zenith lum uncert (%)', 'TotCld (tenths)', 'TotCld source',
#          'TotCld uncert (code)', 'OpqCld (tenths)', 'OpqCld source', 'OpqCld uncert (code)',
#          'Dry-bulb (C)', 'Dry-bulb source', 'Dry - bulb uncert(code)', 'Dew - point(C)', 'Dew - point source',
#          'Dew - point uncert(code)', 'RHum( %)',
#          'RHum source', 'RHum uncert(code)', 'Pressure(mbar)',
#          'Pressure source', 'Pressure uncert(code)', 'Wdir(degrees)',
#          'Wdir source', 'Wdir uncert(code)', 'Wspd(m / s)', 'Wspd source',
#          'Wspd uncert(code)', 'Hvis(m)', 'Hvis source', 'Hvis uncert(code)',
#          'CeilHgt(m)', 'CeilHgt source', 'CeilHgt uncert(code)', 'Pwat(cm)', 'Pwat source',
#          'Pwat uncert(code)', 'AOD(unitless)', 'AOD source', 'AOD uncert(code)',
#          'Alb(unitless)', 'Alb source', 'Alb uncert(code)', 'Lprecip depth(mm)', 'Lprecip quantity(hr)',
#          'Lprecip source', 'Lprecip uncert(code)'])


# try:
#     start_index = cut_bank_muni_ap_map["date"].index(start_date)
# except ValueError:
#     start_index = cut_bank_muni_ap_map["date"][0]
#
# try:
#     end_index = cut_bank_muni_ap_map["date"].index(end_date)
# except ValueError:
#     end_index = cut_bank_muni_ap_map["date"][-1]








