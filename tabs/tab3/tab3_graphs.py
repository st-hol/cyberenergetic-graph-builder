#tod:ax+b
import tkinter as tk
import numpy as np
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties

import view.custom_view as my_view
import tabs.router_page as router
import services.data_service as data_service
import services.tab3_service as tab3_service

import services.util_service as my_service

# 3_1
Q_waste_graph_fig = Figure()
Q_waste_graph_ax = Q_waste_graph_fig.add_subplot(111)

# 3_2
prices_graph_fig = Figure()
prices_graph_ax = prices_graph_fig.add_subplot(111)

# 3_3
warmer_prices_graph_fig = Figure()
warmer_prices_graph_ax = warmer_prices_graph_fig.add_subplot(111)


def animate_Q_waste_graph(i):
    all_data_map = data_service.get_all_data_map()
    is_active = data_service.get_active()
    print("animate active is ", is_active)
    if is_active == "3_1":
        print("dateeee" , data_service.get_date_tab3_interval())
        data_service.update_all_data_map(data_service.get_date_tab3_interval()[0],
                                         data_service.get_date_tab3_interval()[1])

        plot_data = tab3_service.get_all_needed_Q_for_warming_less_than_desired(all_data_map)
        print("3-1 data:", plot_data)
        xs = my_service.restore_lost_data(plot_data[0])
        ys = my_service.restore_lost_data(plot_data[1])
        Q_waste_graph_ax.clear()
        Q_waste_graph_ax.set(xlabel='t ℃ (вісь У)', ylabel='Q, кВт',
                             title='Температурні умови')
        Q_waste_graph_ax.grid()
        Q_waste_graph_ax.plot(xs, ys,
                              # linestyle='-',
                              # linewidth='0.8',
                              markersize=5,
                              label="t ℃ ")


def animate_price_bar_graph(i):
    all_data_map = data_service.get_all_data_map()
    is_active = data_service.get_active()
    if is_active == "3_2":
        data_service.update_all_data_map(data_service.get_date_tab3_interval()[0],
                                         data_service.get_date_tab3_interval()[1])

        prices_graph_ax.set(xlabel='t ℃ (вісь Х)', ylabel='грн. (вісь У)',
                            title='Затрати на опалення відносно температур')
        prices_graph_ax.grid()

        prices_2d_list_of_maps = tab3_service.calc_prices_via_coef(all_data_map)

        width = 1
        for prices in prices_2d_list_of_maps:
            xs = list(prices.keys())
            ys = list(prices.values())
            prices_graph_ax.bar(xs, ys, width,
                                color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                                alpha=0.3)


def animate_warmer_price_bar_graph(i):
    # all_data_map = data_service.get_all_data_map()
    is_active = data_service.get_active()
    if is_active == "3_3":
        # data_service.update_all_data_map(data_service.get_date_tab3_interval()[0],
        #                                  data_service.get_date_tab3_interval()[1])
        warmer_price = tab3_service.obtain_map_price_warmers()
        print(warmer_price)
        xs = list(warmer_price.keys())
        ys = list(warmer_price.values())
        warmer_prices_graph_ax.clear()

        warmer_prices_graph_ax.set(xlabel='t ℃ (вісь Х)', ylabel='грн. (вісь У)',
                            title='Витрати енергії на опалення за визначений період')
        warmer_prices_graph_ax.grid()
        warmer_prices_graph_ax.bar(xs, ys)


class Tab3Graph1_Qwaste(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "3_1":
            data_service.set_active("3_1")
        form_tab3_subtab(self, controller, Q_waste_graph_fig)


class Tab3Graph2_Prices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "3_2":
            data_service.set_active("3_2")
        form_tab3_subtab(self, controller, prices_graph_fig)


class Tab3Graph3_WarmerPrices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "3_3":
            data_service.set_active("3_3")
        form_tab3_subtab(self, controller, warmer_prices_graph_fig)


def form_tab3_subtab(frame, controller, figure):
    button_to_main = tk.Button(frame, text="на головну", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         router.WelcomePage,
                                                                                         "DISABLED"))
    button_to_main.pack()

    button_go_back = tk.Button(frame, text="назад", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab3Page,
                                                                                         "DISABLED"))
    button_go_back.pack()

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab3Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nОберіть процес моделювання:\n\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        graph1_btn = tk.Button(self, text="Залежність тепловтрат будівлі від температурних умов",
                               width=50, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab3Graph1_Qwaste,
                                                                                         "3_1"))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)

        # graph1_btn = tk.Button(self, text="Затрати на опалення відносно температур",
        #                        width=50, bg='lightgreen', fg='blue', relief='flat',
        #                        bd=10, highlightthickness=4, highlightcolor="#37d3ff",
        #                        highlightbackground="#37d3ff", borderwidth=4,
        #                        command=lambda: data_service.display_graph_and_set_active(controller,
        #                                                                                  Tab3Graph2_Prices,
        #                                                                                  "3_2"))
        # graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        # graph1_btn.pack(pady=5, padx=5)

        graph1_btn = tk.Button(self, text="Витрати енергії на опалення за визначений період",
                               width=50, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab3Graph3_WarmerPrices,
                                                                                         "3_3"))
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

        button_set_interval = tk.Button(self, text="Вказати інтервал для температурних даних.",
                                        width=50, bg='lightblue', fg='green', relief='flat',
                                        bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                        highlightbackground="#37d3ff", borderwidth=4,
                                        command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                                  GetInputTab3Frame,
                                                                                                  "DISABLED"))
        button_set_interval.config(font=my_view.CONSOLE_FONT_12)
        button_set_interval.pack(pady=5, padx=5)


class GetInputTab3Frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_to_main = tk.Button(self, text="на головну", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             router.WelcomePage,
                                                                                             "DISABLED"))
        button_to_main.pack()
        button_go_back = tk.Button(self, text="назад", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             Tab3Page,
                                                                                             "DISABLED"))
        button_go_back.pack()

        var_from = tk.StringVar()
        var_to = tk.StringVar()
        N_people = tk.StringVar()
        S = tk.StringVar()
        N_dush = tk.StringVar()
        N_vann = tk.StringVar()
        t_desired = tk.StringVar()

        ent_from = tk.Entry(self, textvariable=var_from)
        ent_from.insert(0, data_service.get_date_tab3_interval()[0])
        ent_to = tk.Entry(self, textvariable=var_to)
        ent_to.insert(0, data_service.get_date_tab3_interval()[1])
        ent_N_people = tk.Entry(self, textvariable=N_people)
        ent_N_people.insert(0, data_service.get_n_people())
        ent_S = tk.Entry(self, textvariable=S)
        ent_S.insert(0, data_service.get_S())
        ent_N_dush = tk.Entry(self, textvariable=N_dush)
        ent_N_dush.insert(0, data_service.get_n_dush())
        ent_N_vann = tk.Entry(self, textvariable=N_vann)
        ent_N_vann.insert(0, data_service.get_n_vann())
        ent_t_desired = tk.Entry(self, textvariable=t_desired)
        ent_t_desired.insert(0, data_service.get_temperature_desired())

        label = tk.Label(self, text=("""\n\n\nФормат введення дати: рік-місяць-день"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='yellow')
        label.pack(pady=2, padx=2)

        label = tk.Label(self, text=("""\n\n\nЗначення дати для початку інтервалу:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_from.pack()

        label = tk.Label(self, text=("""\nЗначення дати для кінця інтервалу:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_to.pack()

        label = tk.Label(self, text=("""\nКількість мешканців:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_N_people.pack()

        label = tk.Label(self, text=("""\nЗначення площі(м^2):"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_S.pack()

        label = tk.Label(self, text=("""\nЗначення Nдуш:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_N_dush.pack()

        label = tk.Label(self, text=("""\nЗначення Nванн:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_N_vann.pack()

        label = tk.Label(self, text=("""\nЗначення бажаної температури (℃):"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_t_desired.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_tab3_data(
                             N_people.get(), S.get(), N_dush.get(), N_vann.get(), t_desired.get(),
                             var_from.get(), var_to.get()))
        btn1.pack(padx=5, pady=5)
