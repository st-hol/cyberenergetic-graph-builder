import pandas as pd
import numpy as np
import math
import numbers
import datetime
import os
import re
#
# import services.tab1_service as tab1_service
# import services.data_service as data_service
#

























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








