import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties

import view.custom_view as my_view
import tabs.router_page as router
import services.data_service as data_service
import services.tab5_service as tab5_service

# 5_1
_5_1_graph_fig = Figure(dpi=80)
_5_1_graph_ax = _5_1_graph_fig.add_subplot(111)


def animate_5_1_graph(i):
    is_active = data_service.get_active()
    print("animate active is ", is_active)
    if is_active == "5_1":
        # map_tab5 = tab5_service.populate_tab5_general_data()
        map_tab5 = tab5_service.tab5_gen_data
        Ts = list(map_tab5[0])
        Hrs = list(map_tab5[1])
        Ps = list(map_tab5[2])
        Qs = list(map_tab5[3])

        # print("LLL:", len(Ts), len(Hrs), len(Ps), len(Qs))

        table_data = []
        for row_i in range(len(Ts)):
            table_data.append([])
            table_data[row_i].append(round(Ts[row_i], 3))
            table_data[row_i].append(round(Hrs[row_i], 3))
            table_data[row_i].append(round(Ps[row_i], 3))
            table_data[row_i].append(round(Qs[row_i], 3))
        # print(table_data)

        table = _5_1_graph_ax.table(cellText=table_data, loc='center', colLabels=["Темпаратура, ℃",
                                                                                  "Сумарна тривалість, год",
                                                                                  "Потужність, кВт",
                                                                                  "Вироблена Енергія, кВт*год"])
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(fontproperties=FontProperties(weight='normal', size=8))
        for key, cell in table.get_celld().items():
            cell.set_linewidth(0.5)

        table_data1 = [
            ["%.2f" % sum(Qs)]
        ]
        table1 = _5_1_graph_ax.table(cellText=table_data1, loc='top', cellLoc='center',
                                     # bbox=[0.76, 0., 0.14, .05])
                                     bbox=[0.70, -0.13, 0.29, .05])
        _5_1_graph_ax.axis('off')
        _5_1_graph_ax.grid()


# 5_2
_5_2_graph_fig = Figure(dpi=80)
_5_2_graph_ax = _5_2_graph_fig.add_subplot(111)


def animate_5_2_graph(i):
    is_active = data_service.get_active()
    print("animate active is ", is_active)
    if is_active == "5_2":

        K_kor_Qtn = tab5_service.calc_K_Qtn_koef()
        Q_rob_TN = tab5_service.calc_Q_rob_TN()
        K_kor_ES = tab5_service.calc_K_kor_ES_koef()
        P_cons_TN = tab5_service.calc_P_consumed_TN()
        N_blocks = tab5_service.calc_N_blocks()
        P_aux_warmer = tab5_service.calc_P_aux_warmer()
        K_zavant = tab5_service.calc_K_zavant()
        P_cyrcyl_nasos = tab5_service.calc_P_cyrcyl_nasos_for_all()
        W_cons_TN = tab5_service.calc_W_cons_TN()
        W_cons_system = tab5_service.calc_W_cons_system()
        Q_tn = tab5_service.calc_Q_TN()
        Q_aux_warmer = tab5_service.calc_Q_aux_warmer()

        table_data = []
        for row_i in range(len(K_kor_Qtn)):
            table_data.append([])
            table_data[row_i].append(round(K_kor_Qtn[row_i], 3))
            table_data[row_i].append(round(Q_rob_TN[row_i], 3))
            table_data[row_i].append(round(K_kor_ES[row_i], 3))
            table_data[row_i].append(round(P_cons_TN[row_i], 3))
            table_data[row_i].append(round(N_blocks[row_i], 3))
            table_data[row_i].append(round(P_aux_warmer[row_i], 3))
            table_data[row_i].append(round(K_zavant[row_i], 3))
            table_data[row_i].append(round(P_cyrcyl_nasos[row_i], 3))
            table_data[row_i].append(round(W_cons_TN[row_i], 3))
            table_data[row_i].append(round(W_cons_system[row_i], 3))
            table_data[row_i].append(round(Q_tn[row_i], 3))
            table_data[row_i].append(round(Q_aux_warmer[row_i], 3))

        # print(table_data)

        table = _5_2_graph_ax.table(cellText=table_data, loc='center', colLabels=["K кор. Qтн",
                                                                                  "Q роб., кВт",
                                                                                  "К кор.ЕС",
                                                                                  "Р спож. ТН., кВт",
                                                                                  "N блоків",
                                                                                  "Р догрівача, кВт",
                                                                                  "К завант.",
                                                                                  "Р цирк. нас., кВт",
                                                                                  "W спож. ТН, кВт*год.",
                                                                                  "W спож. сист, кВт*год.",
                                                                                  "Q тн, кВт*год.",
                                                                                  "Q догр., кВт*год."])
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(fontproperties=FontProperties(weight='normal', size=8))
        for key, cell in table.get_celld().items():
            cell.set_linewidth(0.5)

        table_data1 = [
            ["%.2f" % (sum(W_cons_TN)), "%.2f" % (sum(W_cons_system)), "%.2f" % (sum(Q_tn)), "%.2f" % (sum(Q_aux_warmer))]
        ]
        table1 = _5_2_graph_ax.table(cellText=table_data1, loc='top', cellLoc='center',
                                     bbox=[0.67, -0.13, 0.33, .05])
        # bbox - left bottom angle - x,y,width,height

        _5_2_graph_ax.axis('off')
        _5_2_graph_ax.grid()


class Tab5Graph1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "5_1":
            data_service.set_active("5_1")
        form_tab5_subtab(self, controller, _5_1_graph_fig)


class Tab5Graph2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        is_active = data_service.get_active()
        if is_active != "5_2":
            data_service.set_active("5_2")
        form_tab5_subtab(self, controller, _5_2_graph_fig)


def form_tab5_subtab(frame, controller, figure):
    button_to_main = tk.Button(frame, text="на головну", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         router.WelcomePage,
                                                                                         "DISABLED"))
    button_to_main.pack()

    button_go_back = tk.Button(frame, text="назад", width=40,
                               command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                         Tab5Page,
                                                                                         "DISABLED"))
    button_go_back.pack()

    canvas = FigureCanvasTkAgg(figure, frame)  # canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Tab5Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nОберіть процес моделювання:\n\n"""), font=my_view.CONSOLE_FONT_16)
        label.pack(pady=5, padx=5)
        label.configure(background='black', foreground='lightblue')

        graph1_btn = tk.Button(self, text="Розрахунок потреб у теплі",
                               width=60, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(
                                   controller,
                                   Tab5Graph1,
                                   "5_1"))
        graph1_btn.config(font=my_view.CONSOLE_FONT_12)
        graph1_btn.pack(pady=5, padx=5)

        graph1_btn = tk.Button(self, text="Розрахунок для теплового насоса",
                               width=60, bg='lightgreen', fg='blue', relief='flat',
                               bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                               highlightbackground="#37d3ff", borderwidth=4,
                               command=lambda: data_service.display_graph_and_set_active(
                                   controller,
                                   Tab5Graph2,
                                   "5_2"))
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
                                                                                                  GetInputTab5Frame,
                                                                                                  "DISABLED"))
        button_set_interval.config(font=my_view.CONSOLE_FONT_12)
        button_set_interval.pack(pady=5, padx=5)


class GetInputTab5Frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_to_main = tk.Button(self, text="на головну", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             router.WelcomePage,
                                                                                             "DISABLED"))
        button_to_main.pack()
        button_go_back = tk.Button(self, text="назад", width=40,
                                   command=lambda: data_service.display_graph_and_set_active(controller,
                                                                                             Tab5Page,
                                                                                             "DISABLED"))
        button_go_back.pack()

        n_modules = tk.StringVar()
        ent_n_modules = tk.Entry(self, textvariable=n_modules)
        ent_n_modules.insert(0, data_service.get_tab5_n_modules())
        label = tk.Label(self, text=("""\nКількість модулів :"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_n_modules.pack()

        n_circ_nasos = tk.StringVar()
        ent_n_circ_nasos = tk.Entry(self, textvariable=n_circ_nasos)
        ent_n_circ_nasos.insert(0, data_service.get_tab5_n_circ_nasos())
        label = tk.Label(self, text=("""\nКількість циркуляційних насосів :"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_n_circ_nasos.pack()

        n_funcoyles = tk.StringVar()
        ent_n_funcoyles = tk.Entry(self, textvariable=n_funcoyles)
        ent_n_funcoyles.insert(0, data_service.get_tab5_n_funcoyles())
        label = tk.Label(self, text=("""\nКількість фанкойлів :"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_n_funcoyles.pack()

        power_circ_nasos = tk.StringVar()
        ent_power_circ_nasos = tk.Entry(self, textvariable=power_circ_nasos)
        ent_power_circ_nasos.insert(0, data_service.get_tab5_power_circ_nasos())
        label = tk.Label(self, text=("""\nПотужність циркуляційних насосів :"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_power_circ_nasos.pack()

        power_funcoyles = tk.StringVar()
        ent_power_funcoyles = tk.Entry(self, textvariable=power_funcoyles)
        ent_power_funcoyles.insert(0, data_service.get_tab5_power_funcoyles())
        label = tk.Label(self, text=("""\nПотужність фанкойлів:"""),
                         font=my_view.CONSOLE_FONT_12)
        label.configure(background='black', foreground='green')
        label.pack(pady=3, padx=3)
        ent_power_funcoyles.pack()

        btn1 = tk.Button(self, text="OK",
                         width=10, bg='lightgreen', fg='blue', relief='flat',
                         bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                         highlightbackground="#37d3ff", borderwidth=4,
                         command=lambda: data_service.set_tab5_data(n_modules.get(),
                                                                    n_circ_nasos.get(),
                                                                    n_funcoyles.get(),
                                                                    power_circ_nasos.get(),
                                                                    power_funcoyles.get()
                                                                    ))
        btn1.pack(padx=5, pady=5)
