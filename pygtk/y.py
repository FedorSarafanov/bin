#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
import os
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk
from math import pi

import numpy as np
from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
#Possibly this rendering backend is broken currently
# from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

from matplotlib import animation
import matplotlib.patches as patches
import random
import time


# plt.show()
####################################################



 
class Handler:
	def on_window1_destroy(self, *args):
		Gtk.main_quit(*args)

	# def on_button1_clicked (self, button):
	# 	btn = builder.get_object("button")
	# 	# btn.set_label("Hello World!")

	def cos_clicked (self, button):
		t=np.arange(0,2*np.pi,0.01)
		x=np.cos(t)
		ax.cla()
		ax.plot(t,x)	
		fig.canvas.draw_idle()


	def sin_clicked (self, button):

		t=np.arange(0,2*np.pi,0.01)
		x=np.sin(t)
		ax.cla()
		ax.plot(t,x)	
		fig.canvas.draw_idle()	

	def sq_clicked (self, button):
		tmax=eval(builder.get_object("tmax").get_text())
		tstep=eval(builder.get_object("tstep").get_text())
		t=np.arange(0,tmax,tstep)
		x=t**2
		ax.cla()
		ax.plot(t,x)	
		fig.canvas.draw_idle()			
	def on_eventbox1_button_unpress_event (self, button):
		# label = builder.get_object("label")
		# print(label.get_text())
		pass

fig = Figure(figsize=(1,1), dpi=100)
ax = fig.add_subplot(111)
# t=np.arange(0,2*np.pi,0.01);
# x=np.sin(t);
# ax.plot(t,x)

size=100
t=0
L=5
dt=0.01
g=100
ymin, ymax=-5,5
xmin, xmax=-5,5
r=0.06
k=1
K=1

# fig = plt.figure()
# ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
line, = ax.plot([], [], "ro")

def init():
    line.set_data([], [])
    return line,


# x = np.linspace(0, 2, 1000)
# ax.add_patch(
#     patches.Rectangle(
#         (xmin, ymin),
#         2*xmax,
#         2*ymax,
#         fill=False      # remove background
#     )
# )

v_x=20*np.array([random.uniform(-1,1) for i in range(0,size)])
v_y=20*np.array([random.uniform(-1,1) for i in range(0,size)])

x=L*np.array([random.uniform(0,1) for i in range(0,size)])
y=L*np.array([random.uniform(0,1) for i in range(0,size)])

i1=np.array([0])
i2=np.array([0])
i3=np.array([0])
i4=np.array([0])
T=np.array([0])

def step(dt,x,y,v_x,v_y):
	t=time.time()
	global i1,i2,i3,i4,T

	# обмен скоростями
	N=np.array([])
	for j, elj in enumerate(x):
		for i, el in enumerate(x):
			if (((x[i]-x[j])**2+(y[i]-y[j])**2)<=r**2) and (i!=j):
				if not(i in N):
					N=np.append(N,[i])
				if not(j in N):
					N=np.append(N,[j])					
	N=np.int_(N)

	if len(N)==2:
		i=N[0]
		j=N[1]
		v_x[i],v_x[j]=K*v_x[j],K*v_x[i]
		v_y[i],v_y[j]=K*v_y[j],K*v_y[i]
	else:
		pass

	x=x+v_x*dt
	y=y+v_y*dt

	A=v_y[np.where( y <= ymin )]
	B=v_y[np.where( y >= ymax )]	

	a=np.where( y <= ymin )
	b=np.where( y >= ymax )

	v_y[np.where( y <= ymin )]=-k*v_y[np.where( y <= ymin )]
	i1=np.append(i1, i1[-1]+np.sum(v_y[np.where( y <= ymin )]))
	# print(v_y[np.where( y <= ymin )])
	v_y[np.where( y >= ymax )]=-k*v_y[np.where( y >= ymax )]
	i2=np.append(i2, i2[-1]+np.sum(v_y[np.where( y>= ymax )]))

	v_x[np.where( x <= xmin )]=-k*v_x[np.where( x <= xmin )]
	i3=np.append(i3, i3[-1]+np.sum(v_x[np.where( x <= xmin )]))

	v_x[np.where( x >= xmax )]=-k*v_x[np.where( x >= xmax )]
	i4=np.append(i4, i4[-1]+np.sum(v_x[np.where( x >= xmax )]))

	v_y=v_y-g*dt
	v_y[a]=-k*A
	v_y[b]=-k*B
	T=np.append(T,time.time()-t)
	# T=np.append(T,np.sqrt(np.mean(v_x)**2+np.mean(v_y)**2))
	return x,y,v_x,v_y

def animate(i):
    global x,y, v_x, v_y
    x,y,v_x,v_y=step(dt,x,y,v_x,v_y)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=50000, interval=20, blit=True, repeat=False)


			   
builder = Gtk.Builder()
builder.add_from_file("u.glade")
builder.connect_signals(Handler())
window = builder.get_object("window1") 
sw = builder.get_object("sw") 
canvas = FigureCanvas(fig)
sw.add_with_viewport(canvas)			

# canvas = FigureCanvas(fig)
# canvas.set_size_request(400,400)
# sw.add_with_viewport(canvas)
window.set_size_request(700,500)
window.show_all()
 
Gtk.main()