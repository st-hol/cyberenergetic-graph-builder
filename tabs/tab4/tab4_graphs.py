import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties

import view.custom_view as my_view
import tabs.router_page as router
import services.data_service as data_service
import services.tab4_service as tab4_service

import services.util_service as my_service

# 4_1
_4_1_graph_fig = Figure()
_4_1_graph_ax = _4_1_graph_fig.add_subplot(111)


def animate_4_1_graph(i):
    is_active = data_service.get_active()
    print("animate active is ", is_active)
    if is_active == "4_1":
        map_tab4 = tab4_service.reform_standard_speed_w_map_for_new_h()
        xs = list(map_tab4.keys())
        ys = list(map_tab4.values())
        _4_1_graph_ax.clear()
        # _4_1_graph_ax.axis('equal')
        _4_1_graph_ax.set(xlabel='w, (м/с)', ylabel='W, кВт',
                          title='Енергетична характеристика ВЕУ')
        _4_1_graph_ax.grid()
        _4_1_graph_ax.plot(xs, ys,
                           linestyle='-', linewidth='1',
                           markersize=5,
                           label="t ℃ ")


# 4_2
_4_2_graph_fig = Figure(dpi=80)
_4_2_graph_ax = _4_2_graph_fig.add_subplot(111)


def animate_4_2_graph(i):
    is_active = data_service.get_active()
    print("animate active is ", is_active)
    if is_active == "4_2":
        map_tab4 = tab4_service.reform_standard_speed_w_map_for_new_h()
        speed = list(map_tab4.keys())
        dur = list(data_service.get_tab4_map_speed_dur().values())
        P = list(map_tab4.values())
        E = tab4_service.calc_energy_tab4(map_tab4)

        # print("LLL:", len(speed), len(dur), len(P), len(E))

        table_data = []
        for row_i in range(len(speed)):
            table_data.append([])
            table_data[row_i].append(round(speed[row_i], 3))
            table_data[row_i].append(round(dur[row_i], 3))
            table_data[row_i].append(round(P[row_i], 3))
            table_data[row_i].append(round(E[row_i], 3))
        # print(table_data)

        table = _4_2_graph_ax.table(cellText=table_data, loc='center', colLabels=["швидкість вітру, м/с",
                                                                                  "сумарна тривалість, год",
                                                                                  "Потужність ВЕУ, кВт",
                                                                                  "Вироблена Енергія, кВт*год"])
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(fontproperties=FontProperties(weight='normal', size=10))
        for key, cell in table.get_celld().items():
            cell.set_linewidth(0.5)

        table_data1 = [
            ["Всього енергії вироблено", "%.4f" % tab4_service.calc_sum_energy_tab4(map_tab4) + " кВт*год"],
            ["Дохід від продажу електричної енергії за «зеленим» тарифом", "%.4f" % tab4_service.calc_tab4_income_from_sell_energy(map_tab4) + " €"],
            ["Дохід від продажу одиниць скорочення викидів (ОСВ)", "%.4f" % tab4_service.calc_tab4_income_from_OSV(map_tab4) + " €"]
        ]
        table1 = _4_2_graph_ax.table(cellText=table_data1, loc='bottom', cellLoc='center')

        # table.set_fontsize(14)
        # table.scale(1, 4)
        _4_2_graph_ax.axis('off')
        _4_2_graph_ax.grid()


class Tab4Graph1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "4_1":
            data_service.set_active("4_1")
        form_tab4_subtab(self, controller, _4_1_graph_fig)


class Tab4Graph2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "4_2":
            data_service.set_active("4_2")
        form_tab4_subtab(self, controller, _4_2_graph_fig)

        # tab4_map = tab4_service.reform_standard_speed_w_map_for_new_h()
        #
        # label = tk.Label(self, text="Всього енергії вироблено: "
        #                             + "%.4f" % tab4_service.calc_sum_energy_tab4(tab4_map) + " кВт*год",
        #                  font=my_view.CONSOLE_FONT_12)
        # label.configure(background='black', foreground='green')
        # label.pack(pady=3, padx=3)
        #
        # label = tk.Label(self, text="Дохід від продажу електричної енергії за «зеленим» тарифом : "
        #                             + "%.4f" % tab4_service.calc_tab4_income_from_sell_energy(tab4_map) + " €",
        #                  font=my_view.CONSOLE_FONT_12)
        # label.configure(background='black', foreground='green')
        # label.pack(pady=3, padx=3)
        #
        # label = tk.Label(self, text="Дохід від продажу одиниць скорочення викидів (ОСВ) :"
        #                             + "%.4f" % tab4_service.calc_tab4_income_from_OSV(tab4_map) + " €",
        #                  font=my_view.CONSOLE_FONT_12)
        # label.configure(background='black', foreground='green')
        # label.pack(pady=3, padx=3)


def form_tab4_subtab(frame, controller, figure):
    button_to_main = tk.Button(frame, text="на головну", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         router.WelcomePage,
                                                                                         "DISABLED"))
    button_to_main.pack()

    button_go_back = tk.Button(frame, text="назад", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab4Page,
                                                                                         "DISABLED"))
    button_go_back.pack()

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab4Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nОберіть процес моделювання:\n\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        graph1_btn = tk.Button(self, text="Eнергетична характерисника вітроенергетичної установки",
                               width=60, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(
                                   controller,
                                   Tab4Graph1,
                                   "4_1"))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)

        graph1_btn = tk.Button(self, text="Обсяги генерування енергії ВЕУ ",
                               width=60, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(
                                   controller,
                                   Tab4Graph2,
                                   "4_2"))
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

        button_set_interval = tk.Button(self, text="Вказати дані моделювання",
                                        width=50, bg='lightblue', fg='green', relief='flat',
                                        bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                        highlightbackground="#37d3ff", borderwidth=4,
                                        command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                                  GetInputTab4Frame,
                                                                                                  "DISABLED"))
        button_set_interval.config(font=my_view.CONSOLE_FONT_12)
        button_set_interval.pack(pady=5, padx=5)


class GetInputTab4Frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_to_main = tk.Button(self, text="на головну", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             router.WelcomePage,
                                                                                             "DISABLED"))
        button_to_main.pack()
        button_go_back = tk.Button(self, text="назад", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             Tab4Page,
                                                                                             "DISABLED"))
        button_go_back.pack()

        tower_h = tk.StringVar()
        ent_tower_h = tk.Entry(self, textvariable=tower_h)
        ent_tower_h.insert(0, data_service.get_tab4_tower_h())
        label = tk.Label(self, text=("""\nВисота башти ВЕУ:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_tower_h.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_tab4_data(tower_h.get()))
        btn1.pack(padx=5, pady=5)

        button_to_set_timing = tk.Button(self, text="Корекція характеристики вітрової активності",
                                         width=50, bg='lightgreen', fg='blue', relief='flat',
                                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                         highlightbackground="#37d3ff", borderwidth=4,
                                         command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                                   GetInputTimeUsageFrame,
                                                                                                   "DISABLED"))
        button_to_set_timing.pack(padx=15, pady=15)


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
                                                                                             Tab4Page,
                                                                                             "DISABLED"))
        button_go_back.pack()

        speed_input = tk.StringVar()
        ent_speed_input = tk.Entry(self, textvariable=speed_input)
        ent_speed_input.insert(0, data_service.get_tab4_last_speed())

        dur_input = tk.StringVar()
        ent_dur_input = tk.Entry(self, textvariable=dur_input)
        ent_dur_input.insert(0, data_service.get_tab4_dur_for_this_speed())

        label = tk.Label(self, text=("""\nШвидкість вітру:"""),
                         font=my_view.CONSOLE_FONT_12)

        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_speed_input.pack()

        label = tk.Label(self, text=("""\nТривалість вітрової активності:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_dur_input.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_tab4_speed_dur(speed_input.get(),
                                                                         dur_input.get()))
        btn1.pack(padx=5, pady=5)
