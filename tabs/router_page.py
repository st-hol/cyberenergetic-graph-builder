import tkinter as tk
from tkinter import ttk

import view.custom_view as my_view
import tabs.tab1.tab1_graphs as tab1_graphs
import services.common_service as my_service

all_data_map = my_service.read_xml_all_months()
cut_bank_muni_ap_map = my_service.read_csv()


class PreWelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""
        \nДані для моделювання були завантажені з папки [xlsdata]
        \nВибірка даних відбувається відповідно до шаблону: 
        \n[xlsdata/{місто}-{рік}-{місяць}.xlsx] - для моделювання температурних та вітрових моделей.
        \n[xlsdata/{місто}-data.csv] - для моделювання процесів, пов'язаних з сонячною активністю.
        \nЗауважте, що втрачені комірки будуть відновлені програмно.
        """), font=my_view.CONSOLE_FONT_12)
        label.pack(pady=50, padx=50)
        label.configure(background='black', foreground='green')

        button1 = tk.Button(self, text="Перейти до моделювання",
                            width=40, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(WelcomePage))
        button1.config(font=my_view.CONSOLE_FONT_16)
        button1.pack(pady=50, padx=50)

        button_exit = tk.Button(self, text="вихід",
                                width=40, bg='red', fg='black', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=quit)
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=20, padx=20)


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""\nГоловачук С.В. ТІ-72\nМоделювання кіберенергетичних процесів."""),
                         font=my_view.CONSOLE_FONT_16)
        label.pack(pady=10, padx=10)
        label.configure(background='black', foreground='green')

        label = tk.Label(self, text=("""\n\nОберіть модель:"""),
                         font=my_view.CONSOLE_FONT_16)
        label.pack(pady=10, padx=10)
        label.configure(background='black', foreground='lightblue')

        button1 = tk.Button(self, text="1.Аналіз метеорологічних даних регіону",
                            width=40, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                             command=lambda: controller.show_frame(tab1_graphs.Tab1Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)
        button_exit = tk.Button(self, text="вихід",
                                width=40, bg='red', fg='black', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=quit)
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=20, padx=20)
