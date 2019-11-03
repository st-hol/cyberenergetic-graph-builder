import tkinter as tk
from tkinter import ttk
import re

import view.custom_view as my_view
import tabs.tab1.tab1_graphs as tab1_graphs
import tabs.tab2.tab2_graphs as tab2_graphs
import tabs.tab3.tab3_graphs as tab3_graphs
import tabs.tab4.tab4_graphs as tab4_graphs
import tabs.tab5.tab5_graphs as tab5_graphs
import services.data_service as data_service

# all_data_map = my_service.read_xml_all_months()
# cut_bank_muni_ap_map = my_service.read_csv()


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
                            command=lambda: controller.show_frame(DataInfoPage))
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
                            width=50, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(tab1_graphs.Tab1Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)

        button1 = tk.Button(self, text="2.Моделювання графіка електричного навантаження",
                            width=50, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(tab2_graphs.Tab2Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)

        button1 = tk.Button(self, text="3.Теплотехнічні характеристики будівлі",
                            width=50, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(tab3_graphs.Tab3Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)

        button1 = tk.Button(self, text="4.Визначення ефективності впровадження\nвітроенергетичної установки для потреб\n енергозабезпечення об’єкта ",
                            width=50, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(tab4_graphs.Tab4Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)

        button1 = tk.Button(self, text="5.Визначення ефективності впровадження\nповітряного теплового насосу для потреб\nсистем опалення та кондиціонування об’єкта",
                            width=50, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(tab5_graphs.Tab5Page))
        button1.config(font=my_view.CONSOLE_FONT_12)
        button1.pack(pady=5, padx=5)

        button_exit = tk.Button(self, text="вихід",
                                width=25, bg='red', fg='black', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=quit)
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=20, padx=20)


class DataInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        paths = data_service.obtain_xls_files_from_directory()
        paths = [path[8:] for path in paths]
        filenames_list = ", ".join([path[:-5] for path in paths])
        city_name_search_res = re.search(r'(\D)+-', paths[0])
        city_name = city_name_search_res.group(0).strip('-')
        year_name_search_res = re.search(r'-(\d)+-', paths[0])
        year_name = year_name_search_res.group(0).strip('-')
        monthnames_list = ", ".join([re.search(r'-(\d)+\.', month)
                                    .group(0)
                                    .strip('-')
                                    .strip('.') for month in paths])

        label = tk.Label(self, text=("""\nДані були зчитані з наступних файлів.
        \n{}
        \nДля міста: {}
        \nДля року: {}
        \nДля місяців: {}
        \nЗауважте, що втрачені комірки були відновлені програмно.
        """.format(filenames_list, city_name, year_name, monthnames_list)),
                         font=my_view.CONSOLE_FONT_10)
        label.pack(pady=10, padx=10)
        label.configure(background='black', foreground='green')

        button1 = tk.Button(self, text="Я ознайомився і хочу продовжити",
                            width=40, bg='lightgreen', fg='blue', relief='flat',
                            bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                            highlightbackground="#37d3ff", borderwidth=4,
                            command=lambda: controller.show_frame(WelcomePage))
        button1.config(font=my_view.CONSOLE_FONT_16)
        button1.pack(pady=5, padx=5)
        button_exit = tk.Button(self, text="вихід",
                                width=40, bg='red', fg='black', relief='flat',
                                bd=10, highlightthickness=4, highlightcolor="#37d3ff",
                                highlightbackground="#37d3ff", borderwidth=4,
                                command=quit)
        button_exit.config(font=my_view.CONSOLE_FONT_12)
        button_exit.pack(pady=20, padx=20)
