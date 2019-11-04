import math
import datetime
import random
from collections import OrderedDict

import services.data_service as data_service
import services.tab1_service as tab1_service
import services.tab3_service as tab3_service


##data

def populate_tab5_general_data():
    """
    :return: 2-dimension list
    """
    all_data_map = data_service.read_xml_all_months_with_interval("2012-01-01", "2012-03-01")
    durations = tab1_service.map_temperature_duration(all_data_map)

    sorted_durations = OrderedDict(sorted(durations.items()))
    Ts = list(sorted_durations.keys())
    Hrs = list(sorted_durations.values())
    Ps = [tab3_service.calc_Q_as_q_on_delta_t(t) for t in Ts]
    Q_energy_wasted = [Ps[i] * Hrs[i] for i in range(len(sorted_durations))]
    return [Ts, Hrs, Ps, Q_energy_wasted]


tab5_gen_data = populate_tab5_general_data()


##data


def calc_sum_Q():
    Qs = tab5_gen_data[3]
    return sum(Qs)


def calc_K_Qtn_koef():
    Ts = tab5_gen_data[0]
    min_T = min(Ts)
    max_T = max(Ts)
    min_k = float(math.fabs(min_T) / (math.fabs(min_T) + 0.18 * math.fabs(min_T)))
    max_k = float((math.fabs(max_T) * 0.12 + math.fabs(max_T)) / (math.fabs(max_T)))

    K_Qtn_list = []

    T_eq_ONE_breakpoint_start = Ts.index(-15)
    T_eq_ONE_breakpoint_end = Ts.index(5)

    step = float(max_k - min_k) / (len(Ts))

    print("STEP : ", step)

    min_k_tmp = min_k
    max_k_tmp = 1
    for i in range(len(Ts)):
        if i > T_eq_ONE_breakpoint_start and i < T_eq_ONE_breakpoint_end:
            K_Qtn_list.append(1)
        elif i <= T_eq_ONE_breakpoint_start:
            K_Qtn_list.append(min_k_tmp)
            min_k_tmp += step
        elif i >= T_eq_ONE_breakpoint_end:
            K_Qtn_list.append(max_k_tmp)
            max_k_tmp += step

    return K_Qtn_list
    # return [populate_correct_coef_teploprod(t)
    #         for t in Ts]


def calc_K_kor_ES_koef():
    Ts = tab5_gen_data[0]
    min_T = min(Ts)
    max_T = max(Ts)
    min_k = float(math.fabs(min_T) / (math.fabs(min_T) + 0.12 * math.fabs(min_T)))
    max_k = float((math.fabs(max_T) * 0.12 + math.fabs(max_T)) / (math.fabs(max_T)))

    K_ES_list = []

    T_eq_ONE_breakpoint_start = Ts.index(-12)
    T_eq_ONE_breakpoint_end = Ts.index(0)

    step = float(max_k - min_k) / (len(Ts))

    print("STEP : ", step)

    min_k_tmp = min_k
    max_k_tmp = 1
    for i in range(len(Ts)):
        if i > T_eq_ONE_breakpoint_start and i < T_eq_ONE_breakpoint_end:
            K_ES_list.append(1)
        elif i <= T_eq_ONE_breakpoint_start:
            K_ES_list.append(min_k_tmp)
            min_k_tmp += step
        elif i >= T_eq_ONE_breakpoint_end:
            K_ES_list.append(max_k_tmp)
            max_k_tmp += step

    return K_ES_list
    # return [populate_correct_coef_coldprod(t)
    #         for t in Ts]


def calc_N_blocks():
    return [data_service.get_tab5_n_modules() for t in tab5_gen_data[0]]


CONST_NOMINAL_WARM_CONDUCTIVITY = 8.0  # kWt
CONST_NOMINAL_COLD_CONDUCTIVITY = 7.1  # kWt


#####
def calc_P_consumed_TN():
    Ts = tab5_gen_data[0]
    Ps = tab5_gen_data[2]
    K = calc_K_kor_ES_koef()
    Ps_consumed_TN = [Ps[i] * K[i] for i in range(len(Ts))]
    # Ps_consumed_TN = [Ps[i] * populate_correct_coef_energy_consum_warming_regime(Ts[i]) for i in range(len(Ts))]
    return Ps_consumed_TN


def calc_Q_rob_TN():
    Ts = tab5_gen_data[0]
    Qs = tab5_gen_data[3]
    K = calc_K_Qtn_koef()
    print(len(K), len(Qs), len(Ts))
    Qs_consumed_TN = [Qs[i] * K[i] for i in range(len(Ts))]
    # Qs_consumed_TN = [Qs[i] * populate_correct_coef_teploprod(Ts[i]) for i in range(len(Ts))]
    return Qs_consumed_TN


# Визначитись з кількістю теплових насосів, режимом їх експлуатації та необхідності пікового догрівача.
def calc_P_aux_warmer():
    Qs = tab5_gen_data[3]
    Qs_rob = calc_Q_rob_TN()
    n_modules = data_service.get_tab5_n_modules()
    P_aux_warmer = [(Qs[i] - Qs_rob[i] * n_modules) for i in range(len(Qs))]
    return P_aux_warmer


def calc_K_zavant():
    Qs = tab5_gen_data[3]
    Qs_rob = calc_Q_rob_TN()
    n_modules = data_service.get_tab5_n_modules()
    P_aux_warmer = calc_P_aux_warmer()
    K_zavantazhenya = [float((Qs[i] - P_aux_warmer[i]) / Qs_rob[i] * n_modules) for i in range(len(Qs))]
    return K_zavantazhenya


# 5.7. Визначити загальну фактичну потужність, що споживається всією системою генерування тепла з врахуванням додаткового догрівача для кожного температурного режиму.
def calc_common_power_sgt():
    P_consumed_TN = calc_P_consumed_TN()
    n_modules = data_service.get_tab5_n_modules()
    K_zavant = calc_K_zavant()
    P_aux_warmer = calc_P_aux_warmer()
    common_power_sgt = [P_consumed_TN[i] * n_modules * K_zavant[i] + P_aux_warmer[i] for i in range(len(P_consumed_TN))]
    return common_power_sgt


# 5.8.	 Врахувати потужність споживання системи розподілу енергії (циркуляційні насоси, внутрішні блоки, фанкойли).
def calc_power_syst_cyrcyl():
    p_nasos = data_service.get_tab5_power_circ_nasos()
    p_fancoyl = data_service.get_tab5_power_funcoyles()
    n_nasos = data_service.get_tab5_n_circ_nasos()
    n_fancoyl = data_service.get_tab5_n_funcoyles()
    p_syst_cyrcyl = n_nasos * p_nasos + n_fancoyl * p_fancoyl
    return p_syst_cyrcyl


def calc_P_cyrcyl_nasos_for_all():
    Ts = tab5_gen_data[0]
    P = calc_power_syst_cyrcyl()
    return [P for t in Ts]


def calc_W_cons_TN():
    Q_tn = calc_Q_TN()
    return [Q_tn[i] / 3.5 for i in range(len(Q_tn))]
    # Hrs = tab5_gen_data[1]
    # P_aux_warmer_TN = calc_P_aux_warmer()
    # return [P_aux_warmer_TN[i] * Hrs[i]
    #         for i in range(len(Hrs))]

# Q =t P N k , кВт год
def calc_Q_aux_warmer():
    Hrs = tab5_gen_data[1]
    P_aux_warmer = calc_P_aux_warmer()
    # n_modules = data_service.get_tab5_n_modules()
    # k_zavant = calc_K_zavant()
    return [Hrs[i] * P_aux_warmer[i] for i in range(len(Hrs))]


def calc_W_cons_system():
    P_cyrcyl_nasos = calc_P_cyrcyl_nasos_for_all()
    W_cons_TN = calc_W_cons_TN()
    return [P_cyrcyl_nasos[i] + W_cons_TN[i]
            for i in range(len(W_cons_TN))]


# Теплопродуктивність теплового насоса за певної температури.
# Q =t Q N k , кВт го
def calc_Q_TN():
    Hrs = tab5_gen_data[1]
    Q_rob_TN = calc_Q_rob_TN()
    n_modules = data_service.get_tab5_n_modules()
    k_zavant = calc_K_zavant()
    return [Hrs[i] * Q_rob_TN[i] * n_modules * k_zavant[i]
            for i in range(len(Hrs))]


# Визначити загальні обсяги теплогенерування, електроспоживання і середньозважений СОР системи опалення за розрахунковий період.
def calc_SOR_TN():
    n_modules = data_service.get_tab5_n_modules()
    Hrs = tab5_gen_data[1]
    Qs_rob = calc_Q_rob_TN()
    P_consumed = calc_P_consumed_TN()
    K_zavant = calc_K_zavant()
    #
    sum_1 = sum([Qs_rob[i] * n_modules * K_zavant[i] * Hrs[i] for i in range(len(Hrs))])
    sum_2 = sum([P_consumed[i] * n_modules * K_zavant[i] * Hrs[i] for i in range(len(Hrs))])
    return float(sum_1 / sum_2)


def calc_SOR_syst():
    n_modules = data_service.get_tab5_n_modules()
    Hrs = tab5_gen_data[1]
    Qs_rob = calc_Q_rob_TN()
    P_consumed = calc_P_consumed_TN()
    K_zavant = calc_K_zavant()
    P_aux = calc_P_aux_warmer()
    common_power_sgt = calc_common_power_sgt()
    power_syst_cyrcyl = calc_power_syst_cyrcyl()
    #
    sum_1 = sum([(Qs_rob[i] * n_modules * K_zavant[i] + P_aux[i]) * Hrs[i] for i in range(len(Hrs))])
    sum_2 = sum([(common_power_sgt[i] + power_syst_cyrcyl) * Hrs[i] for i in range(len(Hrs))])
    return float(sum_1 / sum_2)


#  todo percentage
#  todo why Q tn and W aux are the same values
def calc_percanatage_tab5():
    sum_Q = calc_sum_Q()








# ###Корекція теплопродуктивності
# def populate_correct_coef_teploprod(t):
#     if t < -15:
#         return random.uniform(0.75, 1.05)
#     elif t < 5:
#         return 1
#     else:
#         return random.uniform(1.05, 1.3)
#
#
# ###Корекція холодопродуктивності
# def populate_correct_coef_coldprod(t):
#     return random.uniform(1.05, 1.25)
#
#
# ###Корекция споживаної потужності у режимі нагріву
# def populate_correct_coef_energy_consum_warming_regime(t):
#     if t < -10:
#         return random.uniform(1.75, 2.0)
#     elif t < 5:
#         return random.uniform(1.0, 1.5)
#     else:
#         return random.uniform(1.0, 1.3)
#
#
# ###Корекция споживаної потужності у режимі охолодж.
# def populate_correct_coef_energy_consum_colding_regime(t):
#     if t < 15:
#         return random.uniform(0.75, 0.82)
#     else:
#         return random.uniform(0.9, 1.2)
#
#
# # todo import random as ahah)lol
