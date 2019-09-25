import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from tkinter import ttk
from windrose import WindroseAxes

import view.custom_view as my_view
import tabs.router_page as router
import services.tab1_service as tab1_service
import services.common_service as my_service

# 1
temperature_graph_fig = Figure()
temperature_graph_ax = temperature_graph_fig.add_subplot(111)

# 2
temperature_regime_duration_graph_fig = Figure()
temperature_regime_duration_graph_ax = temperature_regime_duration_graph_fig.add_subplot(111)

# 3
windrose_graph_fig = Figure(figsize=(6, 4), dpi=100)
windrose_graph_ax = windrose_graph_fig.add_subplot(111)

# 4
wind_duration_graph_fig = Figure()
wind_duration_graph_ax = wind_duration_graph_fig.add_subplot(111)

# 5
solar_insolation_graph_fig = Figure()
solar_insolation_graph_ax = solar_insolation_graph_fig.add_subplot(111)

# 6
solar_duration_graph_fig = Figure()
solar_duration_graph_ax = solar_duration_graph_fig.add_subplot(111)


def animate_temperature_graph(i):
    xs = my_service.restore_lost_data(router.all_data_map['fullDate'])
    ys = my_service.restore_lost_data(router.all_data_map['T'])
    date = [item.date() for item in xs]
    temperature_graph_ax.clear()
    temperature_graph_ax.set(xlabel='дата', ylabel='t ℃',
                             title='Температурні умови')
    temperature_graph_ax.grid()
    temperature_graph_ax.plot_date(date, ys,
                                   linestyle='-', linewidth='0.3',
                                   markersize=1,
                                   label="t ℃")


def animate_temperature_duration_graph(i):
    map_t_freq = tab1_service.map_temperature_duration(router.all_data_map)
    xs = list(map_t_freq.keys())
    ys = list(map_t_freq.values())
    temperature_regime_duration_graph_ax.clear()

    final_data = [xs, ys]
    table = temperature_regime_duration_graph_ax.table(cellText=final_data, loc='top', cellLoc='center',
                                                       bbox=[0.0, -0.45, 1, .28])
    temperature_regime_duration_graph_fig.subplots_adjust(bottom=0.3)
    table.auto_set_font_size(False)
    table.set_fontsize(5)
    # table.auto_set_column_width((-1, 0, 1, 2, 3))

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(fontproperties=FontProperties(weight='normal', size=4))

    for key, cell in table.get_celld().items():
        cell.set_linewidth(0.1)

    temperature_regime_duration_graph_ax.set(xlabel='t ℃', ylabel='год.',
                                             title='Тривалість температурних режимів')
    temperature_regime_duration_graph_ax.grid()
    temperature_regime_duration_graph_ax.bar(xs, ys)


def animate_windrose_graph(i):
    ws = my_service.restore_lost_data(router.all_data_map['FF'])
    wd = my_service.restore_lost_data(router.all_data_map['dd'])

    ws_scale_1 = tab1_service.map_speed_to_scale_one(ws)
    wd = tab1_service.map_compass_to_degrees(wd)

    # hide axes
    windrose_graph_fig.patch.set_visible(False)
    windrose_graph_ax.axis('off')
    windrose_graph_ax.axis('tight')

    ws_frequency_map = tab1_service.map_ws_by_frequency(ws)
    final_data = [list(ws_frequency_map.keys()), list(ws_frequency_map.values())]
    table = windrose_graph_ax.table(cellText=final_data, loc='top', cellLoc='center',
                                    rowLabels=[" м/с ", " % "], bbox=[0., 0., 0.23, .28])
    windrose_graph_fig.subplots_adjust(bottom=0.6)
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(fontproperties=FontProperties(weight='normal', size=7))
    for key, cell in table.get_celld().items():
        cell.set_linewidth(0.5)

    # windrose_graph_fig.clear()
    rect = [0.1, 0.1, 0.8, 0.8]
    wa = WindroseAxes(windrose_graph_fig, rect)
    windrose_graph_fig.add_axes(wa)
    windrose_graph_ax.grid()
    wa.bar(wd, ws_scale_1, normed=True, opening=0.8, edgecolor='white')
    # wa.set_legend()
    wa.set_legend(title="інтенсивність", loc="upper right")


def animate_wind_duration_graph(i):
    map_t_freq = tab1_service.map_wind_duration(router.all_data_map)
    xs = list(map_t_freq.keys())
    ys = list(map_t_freq.values())
    wind_duration_graph_ax.clear()
    wind_duration_graph_ax.set(xlabel='м/с', ylabel='год.',
                               title='Тривалість режимів вітрової активності вітрів ')
    wind_duration_graph_ax.grid()
    wind_duration_graph_ax.bar(xs, ys)


def animate_insolation_graph(i):
    xs = (router.cut_bank_muni_ap_map['fullDate'])
    ys = (router.cut_bank_muni_ap_map['etrn'])
    # date = [item.date() for item in xs]
    solar_insolation_graph_ax.clear()
    solar_insolation_graph_ax.set(xlabel='дата', ylabel='Вт/м²',
                                  title='Інтенсивність сонячної інсоляції ')
    solar_insolation_graph_ax.grid()
    solar_insolation_graph_ax.bar(xs, ys, width=0.3)


def animate_solar_activity_duration_graph(i):
    map_t_freq = tab1_service.map_solar_activity_duration(router.cut_bank_muni_ap_map)
    xs = list(map_t_freq.keys())
    ys = list(map_t_freq.values())
    xs = my_service.map_to_logarithmic(xs)
    solar_duration_graph_ax.clear()
    solar_duration_graph_ax.set(xlabel='log Вт/м²', ylabel='год.',
                                title='Тривалість режимів сонячної активності')
    solar_duration_graph_ax.grid()
    solar_duration_graph_ax.bar(xs, ys)


class Tab1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nОберіть процес моделювання:\n\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        graph1_btn = tk.Button(self, text="Температурні умови",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph1_TemperatureCond))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)
        graph2_btn = tk.Button(self, text="Тривалість температурних режимів",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph2_TemperatureDuration))
        graph2_btn.config(font=my_view.CONSOLE_FONT_12)
        graph2_btn.pack(pady=5, padx=5)
        graph3_btn = tk.Button(self, text="Троянда вітрів",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph3_WindRose))
        graph3_btn.config(font=my_view.CONSOLE_FONT_12)
        graph3_btn.pack(pady=5, padx=5)
        graph4_btn = tk.Button(self, text="Тривалість режимів вітрової активності",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph4_WindDuration))
        graph4_btn.config(font=my_view.CONSOLE_FONT_12)
        graph4_btn.pack(pady=5, padx=5)
        graph5_btn = tk.Button(self, text="Інтенсивність сонячної інсоляції",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph5_SolarInsolation))
        graph5_btn.config(font=my_view.CONSOLE_FONT_12)
        graph5_btn.pack(pady=5, padx=5)
        graph6_btn = tk.Button(self, text="Тривалість режимів сонячної активності",
                               width=40, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: controller.show_frame(Tab1Graph6_SolarActivityDuration))
        graph6_btn.config(font=my_view.CONSOLE_FONT_12)
        graph6_btn.pack(pady=5, padx=5)

        button_exit = tk.Button(self, text="на головну",
                                width=40, bg='lightgreen', fg='blue', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=lambda: controller.show_frame(router.WelcomePage))
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=20, padx=20)


class Tab1Graph1_TemperatureCond(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, temperature_graph_fig)


class Tab1Graph2_TemperatureDuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, temperature_regime_duration_graph_fig)


class Tab1Graph3_WindRose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, windrose_graph_fig)


class Tab1Graph4_WindDuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, wind_duration_graph_fig)


class Tab1Graph5_SolarInsolation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, solar_insolation_graph_fig)


class Tab1Graph6_SolarActivityDuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        form_tab1_subtab(self, controller, solar_duration_graph_fig)


def form_tab1_subtab(frame, controller, figure):
    # label = tk.Label(frame, text="Змодельовані дані:", font=my_view.LARGE_FONT)
    # label.pack(pady=10, padx=10)

    button_to_main = tk.Button(frame, text="на головну", width=40,
                               command=lambda: controller.show_frame(router.WelcomePage))
    button_to_main.pack()

    button_go_back = tk.Button(frame, text="назад", width=40,
                               command=lambda: controller.show_frame(Tab1Page))
    button_go_back.pack()

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# def supply_val():

#     return [1, 2], [12, 41]
# def animate_temperature_graph(i):
#     xs, ys = supply_val()
#     a.plot(xs, ys)


# for line in a.lines:
#     line.set_marker(None)


# temperature_graph_ax.legend(bbox_to_anchor=(1,1.02,1,.102), loc=3,
#                             ncol=2,borderaxespad=0)
# temperature_graph_ax.set_title("te")


# ws = np.random.random(500) * 6
# wd = np.random.random(500) * 360
