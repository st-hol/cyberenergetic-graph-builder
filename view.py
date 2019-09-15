import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import util

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")
# style.use("fivethirtyeight")

f = Figure()
a = f.add_subplot(111)

def animate(i):
    all_data_2d = util.read_xml_all_months()
    xs = util.restore_lost_data(all_data_2d['fullDate'])
    ys = util.restore_lost_data(all_data_2d['T'])
    date = [item.date() for item in xs]
    a.plot_date(date, ys, linestyle='-', linewidth='0', markersize=3)
    # for line in a.lines:
    #     line.set_marker(None)


def obtainContainer(app):
    container = tk.Frame(app)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    return container


def obtainMenu(container):
    menubar = tk.Menu(container)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="File", menu=filemenu)
    return menubar

def configureWindowView(app):
    # tk.Tk.iconbitmap(self, default="clienticon.ico")
    tk.Tk.wm_title(app, "tab 1")

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        configureWindowView(self)
        container = obtainContainer(self)
        menubar = obtainMenu(container)
        tk.Tk.config(self, menu=menubar)
        self.frames = {}
        all_frames = (WelcomePage, Tab1Page, Tab1Graph1TemperatureConditions)
        for F in all_frames: #todo
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Головачук С.В. \n ТІ-72  \n Варіант №7 """), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="ВКЛАДКА 1", command=lambda: controller.show_frame(Tab1Page))
        button1.pack()
        button2 = ttk.Button(self, text="ВИХІД", command=quit)
        button2.pack()


class Tab1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Оберіть графік:"""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Графік температур",
                             command=lambda: controller.show_frame(Tab1Graph1TemperatureConditions))
        button1.pack()
        button2 = ttk.Button(self, text="test",
                             command=lambda: controller.show_frame(Tab1Graph1TemperatureConditions))
        button2.pack()


        button_exit = ttk.Button(self, text="на головну",
                             command=lambda: controller.show_frame(WelcomePage))
        button_exit.pack()


class Tab1Graph1TemperatureConditions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ГРАФІК", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="НА ГОЛОВНУ",
                             command=lambda:controller.show_frame(WelcomePage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)

        canvas.get_tk_widget().pack()  # canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



app = Application()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()




























# def supply_val():
#     return [1, 2], [12, 41]
# def animate(i):
#     xs, ys = supply_val()
#     a.plot(xs, ys)



