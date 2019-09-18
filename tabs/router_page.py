import tkinter as tk
from tkinter import ttk

import view.custom_view as my_view
import tabs.tab1.tab1_graphs
import services.common_service as my_service


all_data_map = my_service.read_xml_all_months()

cut_bank_muni_ap_map = my_service.read_csv()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=("""\nГоловачук С.В. ТІ-72 Варіант №7 """), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=("""\n[КПІ. ТЕФ. Кіберенергетичні системи]"""), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text=("""\nПрограма для дослідження даних та побудови графіків.\n\n"""), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="ВКЛАДКА 1", command=lambda: controller.show_frame(tabs.tab1.tab1_graphs.Tab1Page))
        button1.pack()
        button2 = ttk.Button(self, text="ВИХІД", command=quit)
        button2.pack()


