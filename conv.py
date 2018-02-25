#!/usr/bin/python

import re
import sys
import random

with open("/home/lab/tex.txt", "r") as ins:
	for line in ins:
		line=line.rstrip()
		with open(line, 'r') as myfile:
			data=myfile.read()
			if data.find(r'\begin{document}')!=-1:
				if data.find(r'\end{document}')!=-1:
					if data.find('tikzpicture')!=-1:
						# print(re.findall(r'\\begin{document}(.*?)\\end{document}', data, re.DOTALL))
						# data=re.findall(r'\\begin{document}(.*?)\\end{document}', data, re.DOTALL)[0]
						for res in re.findall(r'\\begin{tikzpicture}(.*?)\\end{tikzpicture}', data, re.DOTALL):
							res=r'\begin{tikzpicture}'+res+'\n\\end{tikzpicture}';
							hash="%032x" % random.getrandbits(128)
							with open("/home/lab/out/tikzpicture_"+hash+".tex", "w+") as text_file:
								res=r'\documentclass[tikz]{standalone}\input{pre.tex}\begin{document}'+res+r'\end{document}'
								if data.find('begin{axis}')==-1:
									text_file.write(res)

					if data.find('circuitikz')!=-1:
						print('Есть circuitikz!')
						# data=re.findall(r'\\begin{document}(.*?)\\end{document}', data, re.DOTALL)[0]
						for res in re.findall(r'\\begin{circuitikz}(.*?)\\end{circuitikz}', data, re.DOTALL):
							res=r'\begin{circuitikz}'+res+'\n\\end{circuitikz}';
							hash="%032x" % random.getrandbits(128)
							with open("/home/lab/out/circuitikz_"+hash+".tex", "w+") as text_file:
								res=r'\documentclass[tikz]{standalone}\input{pre.tex}\begin{document}'+res+r'\end{document}'
								if data.find('begin{axis}')==-1:
									text_file.write(res)

					if data.find('tikzpict')!=-1:
						print('Есть tikzpict!')
						# data=re.findall(r'\\begin{document}(.*?)\\end{document}', data, re.DOTALL)[0]
						for res in re.findall(r'\\begin{tikzpict}(.*?)\\end{tikzpict}', data, re.DOTALL):
							res=r'\begin{tikzpicture}'+res+'\n\\end{tikzpicture}';
							hash="%032x" % random.getrandbits(128)
							with open("/home/lab/out/tikzpict_"+hash+".tex", "w+") as text_file:
								res=r'\documentclass[tikz]{standalone}\input{pre.tex}\begin{document}'+res+r'\end{document}'
								if data.find('begin{axis}')==-1:
									text_file.write(res)

	# print(hash)

# data=re.findall(r'\\begin{document}(.*?)\\end{document}', data, re.DOTALL)[0]

# print(res)