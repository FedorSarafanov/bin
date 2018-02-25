
import gi
import os
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk 

from random import random
import numpy as np
from multiprocessing.pool import ThreadPool
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib.backends.backend_gtk import FigureCanvasGTK as FigureCanvas
# from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
# from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

# from matplotlib.backends.backend_gtkcairo import FigureCanvasGTKCairo as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

class HelloWorld:
    def __init__(self):
        interface = Gtk.Builder()
        interface.add_from_file('u.glade')

        # self.dialog1 = interface.get_object("dialog1")
        # self.label1 = interface.get_object("label1")
        # self.entry1 = interface.get_object("entry1")
        # self.button1 = interface.get_object("cos_clicked")
        # self.hbox1 = interface.get_object("hbox1")
        self.sw = interface.get_object("sw") 

        # self.fig, self.ax = plt.subplots()
        self.fig = Figure(figsize=(1,1), dpi=100)
        self.ax = self.fig.add_subplot(111)
        # self.line, = self.ax.plot([], [], "ro")
        self.X = [random() for x in range(10)]
        self.Y = [random() for x in range(10)]
        self.line, = self.ax.plot(self.X, self.Y)

        self.canvas = FigureCanvas(self.fig)
        # # self.hbox1.add(self.canvas)
        self.sw.add_with_viewport(self.canvas)

        interface.connect_signals(self)
        # # self.dialog1.show_all()
        window = interface.get_object("window1") 
        window.show_all()        

    def on_window1_destroy(self, widget):
        Gtk.main_quit()

    def sq_clicked(self, widget):
        pass

    def sin_clicked(self, widget):
        pass        

    def cos_clicked(self, widget):
        # name = self.entry1.get_text()
        # self.label1.set_text("Hello " + name)

        self.ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200), init_func=self.init, interval=25, blit=True)
        '''
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(animation.FuncAnimation, args=(self.fig, self.animate, np.arange(1, 200)), kwds={'init_func':self.init, 'interval':25, 'blit':True} )
        self.ani = async_result.get()
        '''
        plt.show()

    def animate(self, i):
        # Read XX and YY from a file or whateve
        XX = [random() for x in range(10)] # just as an example
        YY = [random() for x in range(10)] # just as an example

        self.line.set_xdata( XX )
        self.line.set_ydata( YY )

        return self.line,

    def init(self):
        self.line.set_ydata(np.ma.array(self.X, mask=True))
        return self.line,

# if __name__ == "__main__":
HelloWorld()

Gtk.main()