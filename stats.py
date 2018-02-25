import csv
import numpy as np

hp_1,tp_1=np.array([
    (0, 7.219),
    (5, 8.011), 
    (10,8.703),
    (15,9.428),
    (20,10.096),
    (25,10.829),
    (30,11.520),
    (35,12.197),
    (40,12.989),
    (45,13.651),
    (50,14.327),
    (55,15.033),
    (60,15.791),
    (65,16.549),
    (70,17.307),
    ]).T

tp_1=tp_1-tp_1[0]

with open('experience/pl1.csv', 'w') as csvfile:
    fieldnames = ['s', 't']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writerow({'x': 1, 'y':3})

    writer.writeheader()
    for i in range(0,len(hp_1)):
    	writer.writerow({'s': hp_1[i], 't': tp_1[i]})