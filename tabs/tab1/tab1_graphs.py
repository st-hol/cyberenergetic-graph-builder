import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk
from windrose import WindroseAxes

import view.custom_view as my_view
import tabs.router_page as router
import services.tab1_service as tab1_service
import services.common_service as my_service

#1
temperature_graph_fig = Figure()
temperature_graph_plt = temperature_graph_fig.add_subplot(111)

#2
temperature_regime_duration_graph_fig = Figure()
temperature_regime_duration_graph_plt = temperature_regime_duration_graph_fig.add_subplot(111)

#3
windrose_graph_fig = Figure(figsize=(6, 4), dpi=100)

#4
wind_duration_graph_fig = Figure()
wind_duration_graph_plt = wind_duration_graph_fig.add_subplot(111)


def animate_temperature_graph(i):
    xs = my_service.restore_lost_data(router.all_data_map['fullDate'])
    ys = my_service.restore_lost_data(router.all_data_map['T'])
    date = [item.date() for item in xs]
    temperature_graph_plt.clear()
    temperature_graph_plt.plot_date(date, ys, linestyle='-', linewidth='0', markersize=3)


def animate_temperature_duration_graph(i):
    map_t_freq = tab1_service.map_temperature_duration(router.all_data_map)
    xs = list(map_t_freq.keys())
    ys = list(map_t_freq.values())
    temperature_regime_duration_graph_plt.clear()
    temperature_regime_duration_graph_plt.bar(xs, ys)


def animate_windrose_graph(i):
    # ws = np.random.random(500) * 6
    # wd = np.random.random(500) * 360

    ws = my_service.restore_lost_data(router.all_data_map['FF'])
    wd = my_service.restore_lost_data(router.all_data_map['dd'])

    ws = tab1_service.map_speed_to_scale_one(ws)
    wd = tab1_service.map_compass_to_degrees(wd)

    windrose_graph_fig.clear()
    rect = [0.1, 0.1, 0.8, 0.8]
    wa = WindroseAxes(windrose_graph_fig, rect)
    windrose_graph_fig.add_axes(wa)
    wa.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
    wa.set_legend()


def animate_wind_duration_graph(i):
    map_t_freq = tab1_service.map_wind_duration(router.all_data_map)
    xs = list(map_t_freq.keys())
    ys = list(map_t_freq.values())
    wind_duration_graph_plt.clear()
    wind_duration_graph_plt.bar(xs, ys)


class Tab1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""Оберіть графік:"""), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        graph1_btn = ttk.Button(self, text="Температурні умови",
                             command=lambda: controller.show_frame(Tab1Graph1_TemperatureCond))
        graph1_btn.pack()
        graph2_btn = ttk.Button(self, text="Тривалість температурних режимів",
                                command=lambda: controller.show_frame(Tab1Graph2_TemperatureDuration))
        graph2_btn.pack()
        graph3_btn = ttk.Button(self, text="Троянда вітрів",
                             command=lambda: controller.show_frame(Tab1Graph3_WindRose))
        graph3_btn.pack()
        graph4_btn = ttk.Button(self, text="Тривалість режимів вітрової активності",
                             command=lambda: controller.show_frame(Tab1Graph4_TemperatureDuration))
        graph4_btn.pack()


        button_exit = ttk.Button(self, text="на головну",
                                 command=lambda: controller.show_frame(router.WelcomePage))
        button_exit.pack()


class Tab1Graph1_TemperatureCond(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda: controller.show_frame(router.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(temperature_graph_fig, self)
        # canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab1Graph2_TemperatureDuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda: controller.show_frame(router.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(temperature_regime_duration_graph_fig, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab1Graph3_WindRose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda: controller.show_frame(router.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(windrose_graph_fig, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab1Graph4_TemperatureDuration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda: controller.show_frame(router.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(wind_duration_graph_fig, self)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)





# def supply_val():
#     return [1, 2], [12, 41]
# def animate_temperature_graph(i):
#     xs, ys = supply_val()
#     a.plot(xs, ys)





# for line in a.lines:
#     line.set_marker(None)



