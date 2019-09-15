import tkinter as tk
from tkinter import ttk

import view.custom_view as my_view
import tabs.tab1.tab1_graphs

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Головачук С.В. \n ТІ-72  \n Варіант №7 """), font=my_view.LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="ВКЛАДКА 1", command=lambda: controller.show_frame(tabs.tab1.tab1_graphs.Tab1Page))
        button1.pack()
        button2 = ttk.Button(self, text="ВИХІД", command=quit)
        button2.pack()


