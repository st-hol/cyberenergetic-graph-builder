import tkinter as tk
import numpy as np
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

import view.custom_view as my_view
import tabs.router_page as router
import services.data_service as data_service
import services.tab2_service as tab2_service

import services.util_service as my_service

plt.rcParams.update({'font.size': 8})
plt.xticks(rotation=90)

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
        form_tab2_subtab_for_1_graph(self, controller, _2_1_1_graph_fig)


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
        form_tab2_subtab_for_1_graph(self, controller, _2_1_2_graph_fig)


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
        form_tab2_subtab_for_1_graph(self, controller, _2_1_3_graph_fig)


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
        form_tab2_subtab_for_1_graph(self, controller, _2_1_4_graph_fig)


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
        form_tab2_subtab_for_1_graph(self, controller, _2_1_5_graph_fig)


################################################################################


# 2_2
_2_2_graph_fig = Figure()
_2_2_graph_ax = _2_2_graph_fig.add_subplot(111)


def animate_2_2_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_2":
        all_cons_map = tab2_service.get_all_devices_consumption_that_day()

        xs = list(all_cons_map.keys())
        ys = list(all_cons_map.values())
        _2_2_graph_ax.clear()
        _2_2_graph_ax.set(xlabel='час (вісь Х)', ylabel='W, Вт',
                          title='Сумарний графік навантаження за день')
        _2_2_graph_ax.grid()
        width = np.min(np.diff(mdates.date2num(xs)))
        # Define the date format
        date_form = DateFormatter("%H:%M")
        _2_2_graph_ax.xaxis.set_major_formatter(date_form)
        # Ensure ticks fall once every other week (interval=2)
        _2_2_graph_ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))

        _2_2_graph_ax.bar(xs, ys, width=width, ec="k")


class Tab2Graph6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_2":
            data_service.set_active("2_2")
        form_tab2_subtab_for_full_day(self, controller, _2_2_graph_fig)


#################################

# 2_3
_2_3_graph_fig = Figure()
_2_3_graph_ax = _2_3_graph_fig.add_subplot(111)


def animate_2_3_graph(i):
    is_active = data_service.get_active()
    print("a", is_active)
    if is_active == "2_3":
        # map_day_Wt = tab2_service.get_all_devices_sum_of_consumption_for_each_day()
        map_day_Wt = tab2_service.get_all_devices_sum_of_consumption_for_each_day_by_hrs()
        xs = list(map_day_Wt.keys())
        ys = list(map_day_Wt.values())

        _2_3_graph_ax.clear()
        _2_3_graph_ax.set(xlabel='час', ylabel='W, Вт',
                          title='Тижневий графік навантаження ')
        _2_3_graph_ax.grid()
        for tick in _2_3_graph_ax.get_xticklabels():
            tick.set_rotation(70)
            tick.set_fontsize(4)
        _2_3_graph_ax.plot(xs, ys,
                           linestyle='-', linewidth='2',
                           markersize=4)


class Tab2Graph7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "2_3":
            data_service.set_active("2_3")
        form_tab2_subtab(self, controller, _2_3_graph_fig)


def form_tab2_subtab_for_1_graph(frame, controller, figure):
    # all_measured_devices = list(data_service.get_electric_consumption_devices().keys())
    # all_measured_devices_graphs = [Tab2Graph1,
    #                                Tab2Graph2,
    #                                Tab2Graph3,
    #                                Tab2Graph4,
    #                                Tab2Graph5]

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

    ####
    btn = tk.Button(frame, text="пн", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Mn"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="вт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Tu"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="ср", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Wd"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="чт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Th"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="пт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Fr"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="сб", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Sa"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="нд", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Sn"))
    btn.pack(side=tk.LEFT)
    ####

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


def form_tab2_subtab_for_full_day(frame, controller, figure):
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

    ####
    btn = tk.Button(frame, text="пн", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Mn"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="вт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Tu"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="ср", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Wd"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="чт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Th"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="пт", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Fr"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="сб", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Sa"))
    btn.pack(side=tk.LEFT)
    btn = tk.Button(frame, text="нд", width=4, bg='black', fg='green',
                    command=lambda: data_service.set_tab2_day_of_week("Sn"))
    btn.pack(side=tk.LEFT)
    ####

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


def form_tab2_subtab(frame, controller, figure):
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

        graph1_btn = tk.Button(self, text="Сумарний Г.Е.Н. за день",
                               width=50, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab2Graph6,
                                                                                         "2_2"))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)

        graph1_btn = tk.Button(self, text="Тижневий графік навантаження",
                               width=50, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab2Graph7,
                                                                                         "2_3"))
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

        button_to_set_timing = tk.Button(self, text="Вказати часові інтервали використання приладів",
                                         width=50, bg='lightgreen', fg='blue', relief='flat',
                                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                         highlightbackground="#37d3ff", borderwidth=4,
                                         command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                                   GetInputTimeUsageFrame,
                                                                                                   "DISABLED"))
        button_to_set_timing.pack(padx=15, pady=15)

    # for i in range(len(all_measured_devices_graphs)):
    #     btn = tk.Button(frame, text=str(all_measured_devices[i]), width=8,
    #                     bg='black', fg='green',
    #                     command=lambda: data_service.display_graph_and_set_active(controller,
    #                                                                               all_measured_devices_graphs[i],
    #                                                                               "2_1_" + str(i+1)))
    #     btn.pack(side=tk.RIGHT)


class GetInputTimeUsageFrame(tk.Frame):
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


        name_of_device = tk.StringVar()
        ent_name_of_device= tk.Entry(self, textvariable=name_of_device)
        ent_name_of_device.insert(0, data_service.get_cur_device())

        list_usage = tk.StringVar()
        ent_list_usage = tk.Entry(self, textvariable=list_usage)
        ent_list_usage.insert(0, ','.join(data_service.get_electric_consumption_devices()[data_service.get_cur_device()]
                                          .week_list[data_service.get_cur_day_of_week()]))

        day_of_week = tk.StringVar()
        ent_day_of_week = tk.Entry(self, textvariable=day_of_week)
        ent_day_of_week.insert(0, data_service.get_cur_day_of_week())

        label = tk.Label(self, text=("""\nНазва приладу:(""", ','.join(list(data_service.get_electric_consumption_devices().keys())), ")"),
                         font=my_view.CONSOLE_FONT_12)
        
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_name_of_device.pack()

        label = tk.Label(self, text=("""\nДень використання холодильника:("Mn", "Tu", "Wd", "Th", "Fr", "Sa", "Sn")"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_day_of_week.pack()

        label = tk.Label(self, text=("""\nГодини використання холодильника:(через кому або "fulltime" - для повного дня)"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_list_usage.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_time_for_certain_device(day_of_week.get(), name_of_device.get(), list_usage.get().split(',').copy()))
        btn1.pack(padx=5, pady=5)
