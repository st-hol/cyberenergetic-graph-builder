import pandas as pd
import math
import datetime

def checkIsNan(x):
    if type(x) is datetime.datetime:
        return False
    return math.isnan(x)

def flatten_list(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def read_xml_from_single_report(path):
    all_data_map = {}
    data = pd.read_excel(path)
    days_of_month = pd.DataFrame(data, columns=['Число месяца'])
    UTC = pd.DataFrame(data, columns=['UTC'])
    T = pd.DataFrame(data, columns=['T'])
    dd = pd.DataFrame(data, columns=['dd'])
    FF = pd.DataFrame(data, columns=['FF'])
    ww = pd.DataFrame(data, columns=['ww'])
    N = pd.DataFrame(data, columns=['N'])
    vv = pd.DataFrame(data, columns=['vv'])
    U = pd.DataFrame(data, columns=['U'])
    PPP = pd.DataFrame(data, columns=['PPP'])
    hhh = pd.DataFrame(data, columns=['hhh'])
    all_data_map["days"] = (flatten_list(days_of_month.values))
    all_data_map["UTC"] = (flatten_list(UTC.values))
    all_data_map["T"] = (flatten_list(T.values))
    all_data_map["dd"] = (flatten_list(dd.values))
    all_data_map["FF"] = (flatten_list(FF.values))
    all_data_map["ww"] = (flatten_list(ww.values))
    all_data_map["N"] = (flatten_list(N.values))
    all_data_map["vv"] = (flatten_list(vv.values))
    all_data_map["U"] = (flatten_list(U.values))
    all_data_map["PPP"] = (flatten_list(PPP.values))
    all_data_map["hhh"] = (flatten_list(hhh.values))

    extend_with_full_date(all_data_map, path)
    #print(all_data_map)
    return all_data_map

def extend_with_full_date(all_data_map, path):
    all_data_map["fullDate"] = []
    for day, utc in zip(all_data_map["days"], all_data_map["UTC"]):
        year = path[8:12]
        month = path[13:15]
        month = month.replace(".", "")
        day = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=utc.hour, minute=utc.minute)
        all_data_map["fullDate"].append(day)

def read_xml_all_months():
    months_in_year = 12
    pattern = r'xlsdata/2012-{}.xlsx'
    paths = [pattern.format(i+1) for i in range(months_in_year)]
    all_data_from_all_reports = {}
    all_data_from_all_reports["days"] = []
    all_data_from_all_reports["UTC"] = []
    all_data_from_all_reports["T"] = []
    all_data_from_all_reports["dd"] = []
    all_data_from_all_reports["FF"] = []
    all_data_from_all_reports["ww"] = []
    all_data_from_all_reports["N"] = []
    all_data_from_all_reports["vv"] = []
    all_data_from_all_reports["U"] = []
    all_data_from_all_reports["PPP"] = []
    all_data_from_all_reports["hhh"] = []
    all_data_from_all_reports["fullDate"] = []

    for p in paths:
        all_data_from_current_report = read_xml_from_single_report(p)

        all_data_from_all_reports["days"].extend(all_data_from_current_report["days"])
        all_data_from_all_reports["UTC"].extend(all_data_from_current_report["UTC"])
        all_data_from_all_reports["T"].extend(all_data_from_current_report["T"])
        all_data_from_all_reports["dd"].extend(all_data_from_current_report["dd"])
        all_data_from_all_reports["FF"].extend(all_data_from_current_report["FF"])
        all_data_from_all_reports["ww"].extend(all_data_from_current_report["ww"])
        all_data_from_all_reports["N"].extend(all_data_from_current_report["N"])
        all_data_from_all_reports["vv"].extend(all_data_from_current_report["vv"])
        all_data_from_all_reports["U"].extend(all_data_from_current_report["U"])
        all_data_from_all_reports["PPP"].extend(all_data_from_current_report["PPP"])
        all_data_from_all_reports["hhh"].extend(all_data_from_current_report["hhh"])
        all_data_from_all_reports["fullDate"].extend(all_data_from_current_report["fullDate"])

    return all_data_from_all_reports

def interpolate(l, index):
    middle_ind = int(len(l)/2)
    if index > middle_ind:
        return_value = l[len(l)-1]
        i = middle_ind
        while i < len(l):
            if checkIsNan(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    else:
        return_value = l[0]
        i = 0
        while i < middle_ind:
            if checkIsNan(l[i]):
                i += 1
                continue
            else:
                return_value = l[i]
                break
    return return_value


def restore_lost_data(l):
    restored = l.copy()
    if all(checkIsNan(v) is True for v in l):
        restored = [0 for i in l]
        return restored
    else:
        for i in range(len(l)):
            if checkIsNan(l[i]):
                restored[i] = interpolate(l, i)
        return restored


















# print(read_xml_from_single_report()["hhh"])
# restored = restore_lost_data(read_xml_from_single_report()["hhh"])
# print(restored)
#
# r = restore_lost_data(read_xml_from_single_report()["U"])
# print(r)
# read_xml_from_single_report()
