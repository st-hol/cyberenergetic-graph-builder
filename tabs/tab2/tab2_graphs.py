import tkinter as tk
import numpy as np
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties

import view.custom_view as my_view
import tabs.router_page as router
import services.data_service as data_service
import services.tab2_service as tab2_service

import services.util_service as my_service

# 2_1_1
_2_1_1_graph_fig = Figure()
_2_1_1_graph_ax = _2_1_1_graph_fig.add_subplot(111)


def animate_2_1_1_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_1_1":
        all_devices = data_service.get_electric_consumption_devices()
        intersected_map = tab2_service.intersected_map_of_device_usage(all_devices["fridge"])
        # date = [item.date() for item in xs]

        xs = list(intersected_map.keys())
        ys = list(intersected_map.values())
        print("2_1_1: ", xs, ys)
        _2_1_1_graph_ax.clear()
        _2_1_1_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                            title='Графік навантаження холодильника')
        _2_1_1_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_1_1_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_1_1_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_1_1_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_1_1":
            data_service.set_active("2_1_1")
        form_tab2_subtab(self, controller, _2_1_1_graph_fig)


#########################################


# 2_1_2
_2_1_2_graph_fig = Figure()
_2_1_2_graph_ax = _2_1_2_graph_fig.add_subplot(111)


def animate_2_1_2_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_1_2":
        all_devices = data_service.get_electric_consumption_devices()
        intersected_map = tab2_service.intersected_map_of_device_usage(all_devices["cooker"])
        # date = [item.date() for item in xs]

        xs = list(intersected_map.keys())
        ys = list(intersected_map.values())
        print("2_1_2: ", xs, ys)
        _2_1_2_graph_ax.clear()
        _2_1_2_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                            title='Графік навантаження плити')
        _2_1_2_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_1_2_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_1_2_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_1_2_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_1_2":
            data_service.set_active("2_1_2")
        form_tab2_subtab(self, controller, _2_1_2_graph_fig)


##############################


# 2_1_3
_2_1_3_graph_fig = Figure()
_2_1_3_graph_ax = _2_1_3_graph_fig.add_subplot(111)


def animate_2_1_3_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_1_3":
        all_devices = data_service.get_electric_consumption_devices()
        intersected_map = tab2_service.intersected_map_of_device_usage(all_devices["microwave"])
        # date = [item.date() for item in xs]

        xs = list(intersected_map.keys())
        ys = list(intersected_map.values())
        print("2_1_3: ", xs, ys)
        _2_1_3_graph_ax.clear()
        _2_1_3_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                            title='Графік навантаження мікрохвильової печі')
        _2_1_3_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_1_3_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_1_3_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_1_3_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_1_3":
            data_service.set_active("2_1_3")
        form_tab2_subtab(self, controller, _2_1_3_graph_fig)


################################

# 2_1_4
_2_1_4_graph_fig = Figure()
_2_1_4_graph_ax = _2_1_4_graph_fig.add_subplot(111)


def animate_2_1_4_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_1_4":
        all_devices = data_service.get_electric_consumption_devices()
        intersected_map = tab2_service.intersected_map_of_device_usage(all_devices["teapot"])
        # date = [item.date() for item in xs]

        xs = list(intersected_map.keys())
        ys = list(intersected_map.values())
        print("2_1_4: ", xs, ys)
        _2_1_4_graph_ax.clear()
        _2_1_4_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                            title='Графік навантаження чайника')
        _2_1_4_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_1_4_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_1_4_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_1_4_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_1_4":
            data_service.set_active("2_1_4")
        form_tab2_subtab(self, controller, _2_1_4_graph_fig)


###############################


# 2_1_5
_2_1_5_graph_fig = Figure()
_2_1_5_graph_ax = _2_1_5_graph_fig.add_subplot(111)


def animate_2_1_5_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_1_5":
        all_devices = data_service.get_electric_consumption_devices()
        intersected_map = tab2_service.intersected_map_of_device_usage(all_devices["computer"])
        # date = [item.date() for item in xs]

        xs = list(intersected_map.keys())
        ys = list(intersected_map.values())
        print("2_1_5: ", xs, ys)
        _2_1_5_graph_ax.clear()
        _2_1_5_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                            title='Графік навантаження комп\'ютера')
        _2_1_5_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_1_5_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_1_5_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_1_5_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_1_5":
            data_service.set_active("2_1_5")
        form_tab2_subtab(self, controller, _2_1_5_graph_fig)


###############################


def form_tab2_subtab(frame, controller, figure):
    all_measured_devices = list(data_service.get_electric_consumption_devices().keys())
    all_measured_devices_graphs = [Tab2Graph1,
                                   Tab2Graph2,
                                   Tab2Graph3,
                                   Tab2Graph4,
                                   Tab2Graph5]

    btn = tk.Button(frame, text="холодильник", width=12, bg='black', fg='green',
                    command=lambda: data_service.display_graph_and_set_active(controller, Tab2Graph1, "2_1_1"))
    btn.pack(side=tk.RIGHT)
    btn = tk.Button(frame, text="плита", width=9, bg='black', fg='green',
                    command=lambda: data_service.display_graph_and_set_active(controller, Tab2Graph2, "2_1_2"))
    btn.pack(side=tk.RIGHT)
    btn = tk.Button(frame, text="мікрохв. піч", width=12, bg='black', fg='green',
                    command=lambda: data_service.display_graph_and_set_active(controller, Tab2Graph3, "2_1_3"))
    btn.pack(side=tk.RIGHT)
    btn = tk.Button(frame, text="чайник", width=9, bg='black', fg='green',
                    command=lambda: data_service.display_graph_and_set_active(controller, Tab2Graph4, "2_1_4"))
    btn.pack(side=tk.RIGHT)
    btn = tk.Button(frame, text="комп\'ютер", width=12, bg='black', fg='green',
                    command=lambda: data_service.display_graph_and_set_active(controller, Tab2Graph5, "2_1_5"))
    btn.pack(side=tk.RIGHT)

    button_to_main = tk.Button(frame, text="на головну", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         router.WelcomePage,
                                                                                         "DISABLED"))
    button_to_main.pack()

    button_go_back = tk.Button(frame, text="назад", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab2Page,
                                                                                         "DISABLED"))
    button_go_back.pack()

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nОберіть процес моделювання:\n\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        graph1_btn = tk.Button(self, text="Графіки електричного навантаження",
                               width=50, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab2Graph1,
                                                                                         "2_1_1"))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)

        button_exit = tk.Button(self, text="на головну",
                                width=50, bg='lightgreen', fg='blue', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                          router.WelcomePage,
                                                                                          "DISABLED"))
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=10, padx=10)

        label = tk.Label(self, text=("""\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        button_set_interval = tk.Button(self, text="Вказати дані",
                                        width=50, bg='lightblue', fg='green', relief='flat',
                                        bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                        highlightbackground="#37d3ff", borderwidth=4,
                                        command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                                  GetInputTab2Frame,
                                                                                                  "DISABLED"))
        button_set_interval.config(font=my_view.CONSOLE_FONT_12)
        button_set_interval.pack(pady=5, padx=5)


class GetInputTab2Frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_to_main = tk.Button(self, text="на головну", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             router.WelcomePage,
                                                                                             "DISABLED"))
        button_to_main.pack()
        button_go_back = tk.Button(self, text="назад", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             Tab2Page,
                                                                                             "DISABLED"))
        button_go_back.pack()

        N_people = tk.StringVar()

        ent_N_people = tk.Entry(self, textvariable=N_people)
        ent_N_people.insert(0, data_service.get_n_people())

        label = tk.Label(self, text=("""\nКількість мешканців:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_N_people.pack()

        is_optimized = tk.StringVar()

        ent_is_optimized = tk.Entry(self, textvariable=is_optimized)
        ent_is_optimized.insert(0, "+ " if data_service.get_tab2_optimized() is True else "-")

        label = tk.Label(self, text=("""\nВідображати оптимізовані графіки('+' або '-'):"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_is_optimized.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_tab2_data(N_people.get(), is_optimized.get()))
        btn1.pack(padx=5, pady=5)





    # for i in range(len(all_measured_devices_graphs)):
    #     btn = tk.Button(frame, text=str(all_measured_devices[i]), width=8,
    #                     bg='black', fg='green',
    #                     command=lambda: data_service.display_graph_and_set_active(controller,
    #                                                                               all_measured_devices_graphs[i],
    #                                                                               "2_1_" + str(i+1)))
    #     btn.pack(side=tk.RIGHT)