import math
import datetime
import random

import services.data_service as data_service
import services.tab1_service as tab1_service
import services.util_service as my_service


def calc_Q_dush(N_dush, Q_vann_norm):
    return N_dush * Q_vann_norm


def calc_Q_vann(N_vann, Q_vann_norm):
    return N_vann * Q_vann_norm


def calc_Q_T_dush(Q_dush, T_dush, T_vh_vod, T_vih_vod):
    return Q_dush * ((T_dush - T_vh_vod) / (T_vih_vod - T_vh_vod))


def calc_Q_T_vann(Q_vann, T_vann, T_vh_vod, T_vih_vod):
    return Q_vann * ((T_vann - T_vh_vod) / (T_vih_vod - T_vh_vod))


def calc_Q_T_gar_vod(Q_T_dush, Q_T_vann, po=998.23):
    return (Q_T_dush - Q_T_vann) / po


#############################################################

def calc_W_gar_vod(Q_T_gar_vod, T_baka, T_vh_vod):
    return 1.163 * Q_T_gar_vod * (T_baka - T_vh_vod)


def calc_P_gvp(W_gar_vod, t_nagr):
    return W_gar_vod / t_nagr


#############################################################

def calc_Q_tepl_by_T_rozr_zovn(S_bud, q_tepl):
    return q_tepl * S_bud


#############################################################

def calc_W_tep_i(Qi, Ti):
    return Qi * Ti


# function that filters
def get_months(times):
    counters = {}
    for t in times:
        month = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S").strftime('%m')
        if month in counters:
            counters[month] += 1
        else:
            counters[month] = 1
    return counters


# def calc_average_temperature_per_all_months(all_data_map):
#     distinct_months = get_months(list(all_data_map["T"])).keys()
#     map_t_freq = dict.fromkeys(distinct_temperatures, 0)
#     for t in all_data_map["T"]:
#         map_t_freq[t] += 1
#     map_t_freq = {k: map_t_freq[k] for k in map_t_freq if not math.isnan(k)}
#     return map_t_freq


def get_all_temperatures_sorted(all_data_map):
    l = list(set(all_data_map["T"]))
    l.sort()
    return l


def get_all_temperatures_unsorted(all_data_map):
    l = list(set(all_data_map["T"]))
    # l.sort()
    return l

def calc_q():
    S = int(data_service.get_S())
    return math.fabs(float(S / 100))


def calc_Q_as_q_on_delta_t(t_cur):
    delta_t = int(data_service.get_temperature_desired()) - int(t_cur)
    q = calc_q()
    Q = q * delta_t
    return Q

    # Q += random.randint(0,1)/50
    # Q -= random.randint(0,1)/50

    # diff = Q - math.fabs(Q)
    # if diff > 1e-3:
    #     Q = Q + abs(diff)
    # return Q


def get_all_needed_Q_for_warming_less_than_desired(all_data_map):
    T_list = list(my_service.restore_lost_data(get_all_temperatures_sorted(all_data_map)))
    T_list = filter_t_greater_than_desired(T_list)
    Q_list = [calc_Q_as_q_on_delta_t(t) for t in T_list]
    return (T_list, Q_list)


def get_all_possible_needed_Q_for_warming(all_data_map):
    T_list = list(my_service.restore_lost_data(get_all_temperatures_unsorted(all_data_map)))
    #todo wtf with order aaaa
    Q_list = [calc_Q_as_q_on_delta_t(t) for t in T_list]
    return (T_list, Q_list)


# function that filters
def filter_t_greater_than_desired(temperatures):
    t_desired = data_service.get_temperature_desired()
    res = []
    for t in temperatures:
        if int(t) <= int(t_desired):
            res.append(t)
    return res


# 3.5.	Розрахувати витрати енергії на опалення за визначений період.
def calc_energy_waste_for_certain_period(all_data_map):
    all_possible_map = get_all_possible_needed_Q_for_warming(all_data_map)
    # all_possible_map = get_all_needed_Q_for_warming_less_than_desired(all_data_map)

    all_Q = all_possible_map[0]
    # all_T = all_possible_map[1]
    all_T_map = tab1_service.map_temperature_duration(all_data_map)
    all_T_dur = list(all_T_map.values())
    # print(len(all_T_dur),'and',len(all_Q))
    all_Q = all_Q[:len(all_T_dur)]
    energy_wasted = [all_Q[i] * all_T_dur[i] for i in range(len(all_T_dur))]
    return energy_wasted


def calc_price_by_coef(coef, cur_energy):
    return math.fabs(coef * cur_energy)


# •	теплозабезпечення від централізованої мережі;
# •	автономного теплозабезпечення від газового котла;
# •	автономного теплозабезпечення від вугільного котла;
# •	автономного теплозабезпечення від дров’яного котла;
# •	автономного теплозабезпечення від котла, що працює на деревних пелетах;
# •	автономного теплозабезпечення від електричного котла.

coefs = [1.1, 1.4, 1.8, 2.3, 2.6, 1.65]

# price
def calc_prices_via_coef(all_data_map):
    energy_wasted = calc_energy_waste_for_certain_period(all_data_map)
    Ts = get_all_possible_needed_Q_for_warming(all_data_map)[0]
   # Ts = get_all_needed_Q_for_warming_less_than_desired(all_data_map)[0]

    prices_2d = []
    for coef in coefs:
        prices = dict()
        for energy, t in zip(energy_wasted, Ts):
            price = calc_price_by_coef(coef, energy)
            prices[t] = price
        prices_2d.append(prices.copy())

    [print(item) for item in prices_2d]
    return prices_2d

##################################################################3

OPALYVALNYI_SEASON = 6
# 10 11 12 01 02 03


#Тариф на теплову енергію, грн/Гкал 1292,17
price_on_centralized_net = 1292.17 * 1e-9 * 1e5 *0.9

# теплота згоряння природного газу, Гкал/м3 0,009
# Вартість природного газу грн/м3 3,6
Q_of_gas_burning = 0.009 * 1e9
price_gas_metre3 = 3.6 * 1e5 *2

#Теплота згоряння кам'яного вугілля, Гкал/кг 0,007
#Вартість кам'яного вугілля грн/м3 2,6
Q_of_coal_burning = 0.007 * 1e9
price_coal_metre3 = 2.6 * 1e5 *2

#Теплота згоряння дров, Гкал/кг 0,003
#Вартість дров грн/кг 0,5
Q_of_drova_burning = 0.003 * 1e9
price_drova_metre3 = 0.5 * 1e5 *2

#Теплота згоряння пеллетів, Гкал/кг 0,004
#Вартість пеллетів грн/кг 2,5
Q_of_pellets_burning = 0.004 * 1e9
price_pellets_metre3 = 2.5 * 1e5 *2

#Вартість електричної енергії,  грн/кВт·год 0,456
price_electric_per_vthour = 0.456 * 1e-3 * 1e2 *2
hz_mb_hours = 24*30*OPALYVALNYI_SEASON


def calc_only_opal_season_temperatures():
    print("dates")
    all_data_map = data_service.read_xml_all_months_with_interval("2012-01-01", "2012-03-01")
    print("-dates")
    durations = tab1_service.map_temperature_duration(all_data_map)
    Ts = list(durations.keys())
    Hrs = list(durations.values())
    Q_list = [calc_Q_as_q_on_delta_t(t) for t in Ts]
    print("_____", len(Q_list), "    -_   " , len(Ts),"   __", len(Hrs))
    energy_wasted = [Q_list[i] * Hrs[i] for i in range(len(durations))]
    energy_wasted_for_all_period = sum(energy_wasted)
    print("EEEEE"  , energy_wasted_for_all_period)
    return energy_wasted_for_all_period


def obtain_map_price_warmers():
    energy_wasted_for_all_period = int(calc_only_opal_season_temperatures())

    warmer_price_map = dict()

    #todo calories to Joules
    # Тариф на теплову енергію, грн/Гкал 1292,17
    warmer_price_map["central"] = price_on_centralized_net*energy_wasted_for_all_period

    # теплота згоряння природного газу, Гкал/м3 0,009
    # Вартість природного газу грн/м3 3,6
    # m*0.09 = energy_wasted_for_all_period
    n_metres3_needed = energy_wasted_for_all_period/Q_of_gas_burning
    warmer_price_map["gas"] = n_metres3_needed * price_gas_metre3

    # Теплота згоряння кам'яного вугілля, Гкал/кг 0,007
    # Вартість кам'яного вугілля грн/м3 2,6
    n_metres3_needed = energy_wasted_for_all_period / Q_of_coal_burning
    warmer_price_map["coal"] = n_metres3_needed * price_coal_metre3

    # Теплота згоряння дров, Гкал/кг 0,003
    # Вартість дров грн/кг 0,5
    n_metres3_needed = energy_wasted_for_all_period / Q_of_drova_burning
    warmer_price_map["drova"] = n_metres3_needed * price_drova_metre3

    # Теплота згоряння пеллетів, Гкал/кг 0,004
    # Вартість пеллетів грн/кг 2,5
    n_metres3_needed = energy_wasted_for_all_period / Q_of_pellets_burning
    warmer_price_map["pellets"] = n_metres3_needed * price_pellets_metre3

    # Вартість електричної енергії,  грн/кВт·год 0,456 /// lol
    warmer_price_map["electrics"] = energy_wasted_for_all_period * price_electric_per_vthour

    return warmer_price_map




































