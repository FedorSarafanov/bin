#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from shutil import copyfile
import subprocess
import pyperclip

source=os.path.abspath(__file__)+'gr'
source=source.replace('/labgr','')+'/LAB'
source='/home/lab/bin/LAB'
# print(source)
run_dir=os.path.abspath(os.curdir)

def mkdir(dirr):
    if not os.path.exists(dirr):
        os.makedirs(dirr)

if len(sys.argv)==1:
    title=input("Название лабораторной работы (полное на русском): ")
    name=input("Имя репозитория (одно английское слово): ")
    number=input("Номер лабораторной работы: ")
    group=input("Номер группы (пустой-по умолчанию): ")
    authors=input("Авторы (пустой-по умолчанию): ")

    if group=='':
        group='420'
    if authors=='':
        authors='Понур К.А., Сарафанов Ф.Г., Сидоров Д.А.'      
          
    directory=run_dir+'/'+name;
    mkdir(directory)
    mkdir(directory+'/tables')
    mkdir(directory+'/img')
    mkdir(directory+'/ris')
    mkdir(directory+'/chems')
    mkdir(directory+'/data')
    mkdir(directory+'/text')
    idx=directory+"/"+name+'.tex';

    with open(source+"/index.tex", "r") as lines:
        index=lines.read() # или сразу

    with open(idx, "w+") as f:
        index=index.replace(r'{number}',number)
        index=index.replace(r'{title}',title)
        index=index.replace(r'{group}',group)
        index=index.replace(r'{authors}',authors)
        f.write(index)       

    copyfile(source+'/text/diss.tex', directory+'/text/diss.tex')
    copyfile(source+'/text/titlepage.tex', directory+'/text/titlepage.tex')
    
    subprocess.check_output(['bash','-c', "subl3 "+idx+r":26:10"])
else:
    if (sys.argv[1]=='img') or (sys.argv[1]=='ris'):
        # if len(sys.argv)<3:
        print(run_dir+'/ris')
        if os.path.exists(run_dir+'/ris'):
            if len(sys.argv)<3:
                imgname=input("Имя изображения (на английском): ")
            else:
                imgname=sys.argv[2]
            copyfile(source+'/ris/img.tex', run_dir+'/ris/'+imgname+'.tex')
            subprocess.check_output(['bash','-c', "subl3 "+run_dir+'/ris/'+imgname+'.tex:28:9'])

            with open(source+"/ris/img_.tex", "r") as lines:
                imgg=lines.read() # или сразу
                imgg=imgg.replace(r'{addr}',imgname)
                pyperclip.copy(imgg)   
        else:
            print('Программа запущена вне папки лабораторной!')
    if (sys.argv[1]=='circ') or (sys.argv[1]=='chem'):
        if os.path.exists(run_dir+'/chems'):
            if len(sys.argv)<3:
                imgname=input("Имя схемы (на английском): ")
            else:
                imgname=sys.argv[2]
            copyfile(source+'/chems/circ_.tex', run_dir+'/chems/'+imgname+'.tex')
            subprocess.check_output(['bash','-c', "subl3 "+run_dir+'/chems/'+imgname+'.tex:6:9'])

            with open(source+"/img/img_.tex", "r") as lines:
                imgg=lines.read() # или сразу
                imgg=imgg.replace(r'{addr}',imgname)
                imgg=imgg.replace(r'{fig:',r'{chem:')
                pyperclip.copy(imgg)   
        else:
            print('Программа запущена вне папки лабораторной!')  

    if (sys.argv[1]=='plot') or (sys.argv[1]=='graph'):
        if os.path.exists(run_dir+'/img'):
            if len(sys.argv)<3:
                imgname=input("Имя графика (на английском): ")
            else:
                imgname=sys.argv[2]

            if len(sys.argv)<4:
                TABLE=imgname
                XDATA='x'
                XLABEL=r'$x$'
                YLABEL=r'$y$'
                YDATA='y'                           
            else:
                if sys.argv[3]=='set':
                    TABLE=input("Имя исходной таблицы в data, без путей: ")
                    if TABLE=='':
                        TABLE==imgname+'.tsv'
                    XDATA=input("x column: ")
                    YDATA=input("y column: ")
                    XLABEL=input("x label: ")
                    YLABEL=input("y label: ")  

            # copyfile(source+'/img/plot.tex', run_dir+'/img/'+imgname+'.tex')

            with open(source+'/img/plot.tex', "r") as f:
                index=f.read()
                index=index.replace(r'XDATA',XDATA)
                index=index.replace(r'YDATA',YDATA)
                index=index.replace(r'XLAB',XLABEL)
                index=index.replace(r'YLAB',YLABEL)
                index=index.replace(r'TABLE',TABLE)
                # f.write(index)       
            with open(run_dir+'/img/'+imgname+'.tex', "w+") as f:
                f.write(index)                        

            subprocess.check_output(['bash','-c', "subl3 "+run_dir+'/img/'+imgname+'.tex:8:24'])

            with open(source+"/img/img_.tex", "r") as lines:
                imgg=lines.read() # или сразу
                imgg=imgg.replace(r'{addr}',imgname)
                imgg=imgg.replace(r'{fig:',r'{graph:')
                pyperclip.copy(imgg)   
        else:
            print('Программа запущена вне папки лабораторной!')                  

# def display_title_bar():
#     # Clears the terminal screen, and displays a title bar.
#     os.system('clear')
              
#     print("\t**********************************************")
#     print("\t*******  Создание лабораторной работы  *******")
#     print("\t**********************************************")


# def print_choice_list(keys):
#     choices=[]
#     display_title_bar()
#     print("\n")
#     for key in keys:
#         print('['+key+'] '+keys[key])
#         choices.append(key)
#     return choices

# def get_user_choice(keys):
#     choices=print_choice_list(keys)
#     choice='afjdsklalsdklfhasldjkfhlasdjfhasjdfhajl'
#     while not(choice in choices):
#         choices=print_choice_list(keys)
#         choice=input("Выбор: ")
#     return choice
    

# display_title_bar()
  
    
# choice = get_user_choice({'1':'Создание лабораторной работы','2':'','q':'выйти'})

