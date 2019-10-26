import math
import datetime
import random

import services.data_service as data_service
import services.tab1_service as tab1_service
import services.util_service as my_service



##
# Потужність, кВт Швидкість вітру м/с
dirty = "0 0 0 1 0.5 2 1 3 1.5 4 1.8 5 2.3 6 3 7 3.5 8 4.1 9 4.7 10 4.9 11 5.3 12 5.8 13 6 14 6.2 15 6.4" \
        " 16 6.8 17 7 18 7.1 19 7.2 20 7.2 21 7.2 22".split(" ")


def get_map_speed_power_for_h_10():
    i = 0
    speed = []
    W = []
    while i < len(dirty):
        if i % 2 == 1:
            speed.append(dirty[i])
        elif i % 2 == 0:
            W.append(dirty[i])
        i += 1
    map_speed_power = dict(zip(speed, W))
    return map_speed_power


def calc_speed_for_certain_h(speed_cur, h_cur, h_new):
    print(speed_cur * (float(math.pow(float(h_new) / float(h_cur), 0.14))))
    return speed_cur * (float(math.pow(float(h_new) / float(h_cur), 0.14)))


def calc_tab4_coef():
    return 1 + data_service.get_tab4_tower_h() * 0.003


def reform_standard_speed_w_map_for_new_h():
    map_speed_power_for_h_10 = get_map_speed_power_for_h_10()
    if data_service.get_tab4_tower_h() == 10:
        return map_speed_power_for_h_10
    else:
        reformed_map = dict()
        for key, value in map_speed_power_for_h_10.items():
            speed_cur = float(key)
            h_vidome = 10
            h_new = data_service.get_tab4_tower_h()
            reformed_map[calc_speed_for_certain_h(speed_cur, h_vidome, h_new)] = (
                0.13 if value == 0 else float(value) * calc_tab4_coef())
    return reformed_map


def calc_energy_tab4(map_speed_power):
    speeds = list(data_service.tab4_map_speed_dur.keys())
    times = list(data_service.tab4_map_speed_dur.values())
    Ps = [float(i) for i in list(map_speed_power.values())]
    # kWt*hod
    return [times[i] * Ps[i] for i in range(len(times))]


def calc_sum_energy_tab4(map_speed_power):
    return sum(calc_energy_tab4(map_speed_power))


# 4.5.Провести оцінкуобсягів скорочень викидів парникових газів у тонах СО2 еквіваленту. У порівнянні з базовим сценарієм.
def calc_co2_tab4(map_speed_power):
    """
        :return tones
    """
    total_sum_energy = calc_sum_energy_tab4(map_speed_power) / 1e3  # to Mwt
    return 1.06 * total_sum_energy


# Вартість 1 кВт∙год за «зеленим» тарифом для вітроенергетики складає 0,11€
const_price_for_1point_of_energy = 0.11


def calc_tab4_income_from_sell_energy(map_speed_power):
    total_E = calc_sum_energy_tab4(map_speed_power)  # kwt
    total_E -= data_service.recalc_tab4_uec(map_speed_power)
    if total_E <= 0:
        return 0
    return total_E * const_price_for_1point_of_energy


# Дохід від продажу одиниць скорочення викидів (ОСВ)
# Ціна на ОСВ: 10 €/тонну СО2 екв.
const_price_for_OSV = 10


def calc_tab4_income_from_OSV(map_speed_power):
    total_tonnes = calc_co2_tab4(map_speed_power)
    return total_tonnes * const_price_for_OSV
