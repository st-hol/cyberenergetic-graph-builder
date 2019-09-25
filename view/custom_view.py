import tkinter as tk

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def obtain_container(app):
    container = tk.Frame(app)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    return container


def obtain_menu(container):
    menubar = tk.Menu(container)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Вихід", command=quit)
    menubar.add_cascade(label="Файл", menu=filemenu)
    return menubar


def configure_window_view(app):
    tk.Tk.iconbitmap(app, default="favicon.ico")
    tk.Tk.wm_title(app, "Моделювання кіберенергетичних процесів.")