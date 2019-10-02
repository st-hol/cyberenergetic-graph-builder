import matplotlib
import matplotlib.animation as animation
import tkinter as tk

import view.custom_view as my_view
import tabs.router_page as welcome
import tabs.tab1.tab1_graphs as tab1_graphs
import tabs.tab3.tab3_graphs as tab3_graphs

matplotlib.use("TkAgg")
# style.use("ggplot")  # style.use("fivethirtyeight")


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        my_view.configure_window_view(self)
        container = my_view.obtain_container(self)
        menubar = my_view.obtain_menu(container)
        tk.Tk.config(self, menu=menubar)
        self.frames = {}

        all_frames = (welcome.PreWelcomePage,
                      welcome.WelcomePage,
                      welcome.DataInfoPage,
                      tab1_graphs.Tab1Page,
                      tab1_graphs.GetInput1Frame,
                      tab1_graphs.GetInput2Frame,
                      tab1_graphs.Tab1Graph1_TemperatureCond,
                      tab1_graphs.Tab1Graph2_TemperatureDuration,
                      tab1_graphs.Tab1Graph3_WindRose,
                      tab1_graphs.Tab1Graph4_WindDuration,
                      tab1_graphs.Tab1Graph5_SolarInsolation,
                      tab1_graphs.Tab1Graph6_SolarActivityDuration,

                      tab3_graphs.Tab3Page)

        for F in all_frames:
            frame = F(container, self)
            frame.configure(background='black')
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(welcome.PreWelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__':
    app = Application()
    app.geometry("1376x768")
    temperature_graph_ani = animation.FuncAnimation(tab1_graphs.temperature_graph_fig,
                                                    tab1_graphs.animate_temperature_graph, interval=10000)
    windrose_graph_ani = animation.FuncAnimation(tab1_graphs.windrose_graph_fig,
                                                 tab1_graphs.animate_windrose_graph, interval=10000)
    temperature_duration_graph_ani = animation.FuncAnimation(tab1_graphs.temperature_regime_duration_graph_fig,
                                                             tab1_graphs.animate_temperature_duration_graph,
                                                             interval=20000)
    wind_graph_ani = animation.FuncAnimation(tab1_graphs.wind_duration_graph_fig,
                                             tab1_graphs.animate_wind_duration_graph, interval=20000)
    solar_insolation_graph_ani = animation.FuncAnimation(tab1_graphs.solar_insolation_graph_fig,
                                                         tab1_graphs.animate_insolation_graph, interval=30000)
    solar_activity_duration_graph_ani = animation.FuncAnimation(tab1_graphs.solar_duration_graph_fig,
                                                                tab1_graphs.animate_solar_activity_duration_graph,
                                                                interval=30000)
    app.mainloop()
