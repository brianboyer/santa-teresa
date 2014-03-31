# -*- coding: utf-8 -*-
import csv

usos = []

with open('input/Pozos20140313SenaraCRTMW05GS84.csv', 'rb') as pozosfile:
    pozosreader = csv.DictReader(pozosfile, delimiter=',', quotechar='"')
    print "aguauso"
    for row in pozosreader:
        if row['aguauso'] in usos:
            pass
        else:
            print row['aguauso']
            usos.append(row['aguauso'])
            