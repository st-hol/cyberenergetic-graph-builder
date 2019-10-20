import matplotlib
import matplotlib.animation as animation
# from matplotlib import style
import tkinter as tk

import view.custom_view as my_view
import tabs.router_page as welcome
import tabs.tab1.tab1_graphs as tab1_graphs
import tabs.tab2.tab2_graphs as tab2_graphs
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

                      tab2_graphs.Tab2Page,
                      tab2_graphs.Tab2Graph1,
                      tab2_graphs.Tab2Graph2,
                      tab2_graphs.Tab2Graph3,
                      tab2_graphs.Tab2Graph4,
                      tab2_graphs.Tab2Graph5,
                      tab2_graphs.GetInputTab2Frame,
                      tab2_graphs.Tab2Graph6,
                      tab2_graphs.Tab2Graph7,

                      tab3_graphs.Tab3Page,
                      tab3_graphs.GetInputTab3Frame,
                      tab3_graphs.Tab3Graph1_Qwaste,
                      tab3_graphs.Tab3Graph2_Prices,
                      tab3_graphs.Tab3Graph3_WarmerPrices)

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
                                                    tab1_graphs.animate_temperature_graph, interval=3000)
    windrose_graph_ani = animation.FuncAnimation(tab1_graphs.windrose_graph_fig,
                                                 tab1_graphs.animate_windrose_graph, interval=3000)
    temperature_duration_graph_ani = animation.FuncAnimation(tab1_graphs.temperature_regime_duration_graph_fig,
                                                             tab1_graphs.animate_temperature_duration_graph,
                                                             interval=3000)
    wind_graph_ani = animation.FuncAnimation(tab1_graphs.wind_duration_graph_fig,
                                             tab1_graphs.animate_wind_duration_graph, interval=3000)
    solar_insolation_graph_ani = animation.FuncAnimation(tab1_graphs.solar_insolation_graph_fig,
                                                         tab1_graphs.animate_insolation_graph, interval=3000)
    solar_activity_duration_graph_ani = animation.FuncAnimation(tab1_graphs.solar_duration_graph_fig,
                                                                tab1_graphs.animate_solar_activity_duration_graph,
                                                                interval=3000)

    ####################################################################################################################
    Q_waste_graph_ani = animation.FuncAnimation(tab3_graphs.Q_waste_graph_fig,
                                                tab3_graphs.animate_Q_waste_graph,
                                                interval=3000)
    # prices_graph_ani = animation.FuncAnimation(tab3_graphs.prices_graph_fig,
    #                                            tab3_graphs.animate_price_bar_graph,
    #                                            interval=3000)
    warmer_prices_graph_ani = animation.FuncAnimation(tab3_graphs.warmer_prices_graph_fig,
                                                      tab3_graphs.animate_warmer_price_bar_graph,
                                                      interval=3000)

    ####################################################################################################################

    _2_1_1_graph_ani = animation.FuncAnimation(tab2_graphs._2_1_1_graph_fig,
                                               tab2_graphs.animate_2_1_1_graph,
                                               interval=5000)

    _2_1_2_graph_ani = animation.FuncAnimation(tab2_graphs._2_1_2_graph_fig,
                                               tab2_graphs.animate_2_1_2_graph,
                                               interval=5000)

    _2_1_3_graph_ani = animation.FuncAnimation(tab2_graphs._2_1_3_graph_fig,
                                               tab2_graphs.animate_2_1_3_graph,
                                               interval=5000)

    _2_1_4_graph_ani = animation.FuncAnimation(tab2_graphs._2_1_4_graph_fig,
                                               tab2_graphs.animate_2_1_4_graph,
                                               interval=5000)

    _2_1_5_graph_ani = animation.FuncAnimation(tab2_graphs._2_1_5_graph_fig,
                                               tab2_graphs.animate_2_1_5_graph,
                                               interval=5000)
    ##
    _2_2_graph_ani = animation.FuncAnimation(tab2_graphs._2_2_graph_fig,
                                               tab2_graphs.animate_2_2_graph,
                                               interval=5000)
    ##
    _2_3_graph_ani = animation.FuncAnimation(tab2_graphs._2_3_graph_fig,
                                               tab2_graphs.animate_2_3_graph,
                                               interval=5000)

    app.mainloop()




