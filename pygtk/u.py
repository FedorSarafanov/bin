#!/usr/bin/python3
# coding: utf-8
import sys
import os

# try:
# import pyGtk
# pyGtk.require('3.0')
# except:
		# sys.exit(1)
# try:

# import Gtk
# import Gtk.gladeimport gi
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 
# except:
		# sys.exit(1)
		
class App:
	def __init__(self):
		builder = Gtk.Builder()
		builder.new_from_file("pygtk001.glade")		
		handlers = {
			"button1_clicked_cb" : self.text_operation,
			"button2_clicked_cb": self.text_operation,
		}
		builder.connect_signals(handlers)		

		window = builder.get_object("window1")
		window.show_all()		  
		# Магическая команда, соединяющая сигналы с обработчиками
		# self.widgetsTree.signal_autoconnect(dic)
		# Соединяем событие закрытия окна с функцией завершения приложения
		self.window = self.widgetsTree.get_widget("window1")
		if (self.window):
			self.window.connect("destroy", self.close_app)
		# А это уже логика приложения. Задём маршруты обработки текста для каждой кнопки.
		# Первый элемент - имя виджета-источника текста, второй - имя виджета-получателя  
		self.routes = {'button1': ('textview1','textview2'),
				   'button2': ('textview2','textview1')}

	def text_operation(self,widget):
		"Функция, которая перебрасывает текст туда-сюда"
		# виджет-источник
		source = self.widgetsTree.get_widget(self.routes[widget.name][0])
		# виджет-получатель
		destination = self.widgetsTree.get_widget(self.routes[widget.name][1])
		# текстовый буфер источника
		source_text_buffer = source.get_buffer()
		# массив итераторов границ текста в текстовом буфере источника (начало и конец)
		source_text_buffer_bounds = source_text_buffer.get_bounds()
		# собственно текст
		source_text = source_text_buffer.get_text(source_text_buffer_bounds[0],
												  source_text_buffer_bounds[1])
		# устанавливаем текст в текстовом буфере виджета-получателя
		destination.get_buffer().set_text(source_text)
		# очищаем текстовый буфер источника
		source_text_buffer.set_text('')
		   
	def close_app(self, widget):	
		Gtk.main_quit()		
	
if __name__ == "__main__":
	app = App()
	Gtk.main()