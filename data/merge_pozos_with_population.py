# -*- coding: utf-8 -*-
import csv

poblacion_por_distrito = {}

with open('input/poblacion_por_distrito.csv', 'rb') as poblacionfile:
    poblacionreader = csv.DictReader(poblacionfile, delimiter=',', quotechar='"')
    for row in poblacionreader:

        codigo = row['codigo']
        poblacion = row['poblacion']
        nombre = row['nombre']
        
        poblacion_por_distrito[codigo] = {'poblacion':poblacion,'nombre':nombre,'codigo':codigo}

with open('output/distritos.csv', 'rb') as distritosfile:
    distritosreader = csv.DictReader(distritosfile, delimiter=',', quotechar='"')
    for row in distritosreader:
        
        codigo = row['codigo']
        
        district = poblacion_por_distrito[codigo]
        district['provincia'] = row['provincia']
        district['canton'] = row['canton']
        district['caudal'] = row['caudal']
        district['pozos'] = row['pozos']
    
        poblacion_por_distrito[codigo] = district

with open('input/classificacion_por_distrito.csv') as classificacionfile:
    classificacionreader = csv.DictReader(classificacionfile, delimiter=',', quotechar='"')
    for row in classificacionreader:
        
        codigo = row['Código']

        district = poblacion_por_distrito[codigo]
        district['region de consumo'] = row['Región']
        district['consumo promedio mensual en metros cubicos'] = row['Consumo promedio mensual m3']
        district['consumo diario en litros'] = row['Consumo diario en litros']
    
with open('output/merged.csv','wb') as mergedfile:
    mergedwriter = csv.DictWriter(mergedfile, ['codigo','nombre','poblacion','provincia','canton','caudal','pozos','region de consumo','consumo promedio mensual en metros cubicos','consumo diario en litros'])
    mergedwriter.writeheader()
    mergedwriter.writerows(poblacion_por_distrito.values())
