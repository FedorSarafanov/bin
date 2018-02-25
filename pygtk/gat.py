# import gtk
import gi
import os
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk
# from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
# from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


class MyProgram():
    def __init__(self):
        #some_gtk_stuff
        self.builder=Gtk.Builder()
        self.builder.add_from_file("u.glade")
        self.window = self.builder.get_object("window1") 
        # sw = builder.get_object("sw") 
        # canvas = FigureCanvas(fig)
        # sw.add_with_viewport(canvas)                
        self.signals = {
                'cos_clicked': self.create_plot,
                'sin_clicked': self.create_plot,
                'sq_clicked': self.create_plot,
                'on_window1_destroy': self.on_window1_destroy,
        }
        self.builder.connect_signals(self.signals)

        self.vbox = self.builder.get_object('vbox')

        self.figure = plt.figure(figsize=(1,1), dpi=100)
        # self.axis = self.figure.add_subplot(111)
        # self.figure = Figure(figsize=(1,1), dpi=100)
        self.ax = self.figure.add_subplot(111)        
        self.canvas = None

        self.window.set_size_request(700,500)
        self.window.show_all()

    def create_plot(self, button):
        self.ani = animation.FuncAnimation(self.figure, self.update_plot, interval = 1000)

    def on_window1_destroy(self, *args):
        Gtk.main_quit(*args)

    def update_plot(self, i):
        #read SampleData from txt File
        x = []
        y = []
        with open('s.dat') as f:
            x_raw, y_raw = f.readline().strip().split(',')
            x.append(int(x_raw))
            y.append(int(y_raw))

        self.axis.plot(x, y)

        if not self.canvas:
            self.canvas = FigureCanvas(self.figure)
            self.vbox.pack_start(self.canvas)
            self.canvas.show()

        self.canvas.draw()

MyProgram()
Gtk.main()