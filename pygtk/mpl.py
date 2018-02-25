#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk

import numpy as np
from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

myfirstwindow = Gtk.Window()
myfirstwindow.connect("delete-event", Gtk.main_quit)
myfirstwindow.set_default_size(400, 400)

fig = Figure(figsize=(5,5), dpi=100)
ax = fig.add_subplot(111)
t=np.arange(0,2*np.pi,0.01);
x=np.sin(t);
ax.plot(t,x)

sw = Gtk.ScrolledWindow()
myfirstwindow.add(sw)

canvas = FigureCanvas(fig)
canvas.set_size_request(400,400)
sw.add_with_viewport(canvas)

myfirstwindow.show_all()
Gtk.main()