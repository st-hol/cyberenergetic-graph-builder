import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk
from windrose import WindroseAxes

import view.custom_view as my_view
import tabs.router_page as welcome
import util

temperature_graph_fig = Figure()
temperature_graph_plt = temperature_graph_fig.add_subplot(111)

temperature_regime_duration_graph_fig = Figure()
temperature_regime_duration_graph_plt = temperature_regime_duration_graph_fig.add_subplot(111)

windrose_graph_fig = Figure(figsize=(6, 4), dpi=100)


def animate_temperature_graph(i):
    all_data_2d = util.read_xml_all_months()
    xs = util.restore_lost_data(all_data_2d['fullDate'])
    ys = util.restore_lost_data(all_data_2d['T'])
    date = [item.date() for item in xs]
    temperature_graph_plt.clear()
    temperature_graph_plt.plot_date(date, ys, linestyle='-', linewidth='0', markersize=3)


def animate_temperature_duration_graph(i):
    pass


def animate_windrose_graph(i):
    ws = np.random.random(500) * 6
    wd = np.random.random(500) * 360

    windrose_graph_fig.clear()
    rect = [0.1, 0.1, 0.8, 0.8]
    wa = WindroseAxes(windrose_graph_fig, rect)
    windrose_graph_fig.add_axes(wa)
    wa.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
    wa.set_legend()


class Tab1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Оберіть графік:"""), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Графік температур",
                             command=lambda: controller.show_frame(Tab1Graph1_TemperatureCond))
        button1.pack()
        button2 = ttk.Button(self, text="test",
                             command=lambda: controller.show_frame(Tab1Graph3_WindRose))
        button2.pack()

        button_exit = ttk.Button(self, text="на головну",
                                 command=lambda: controller.show_frame(welcome.WelcomePage))
        button_exit.pack()


class Tab1Graph1_TemperatureCond(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda: controller.show_frame(welcome.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(temperature_graph_fig, self)
        # canvas.show()
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
                             command=lambda: controller.show_frame(welcome.WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(windrose_graph_fig, self)
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



