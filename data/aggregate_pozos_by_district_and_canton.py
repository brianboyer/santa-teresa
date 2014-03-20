# -*- coding: utf-8 -*-
import csv
from decimal import *

distritos = {}

with open('input/pozos.csv', 'rb') as pozosfile:
    pozosreader = csv.DictReader(pozosfile, delimiter=',', quotechar='"')
    for row in pozosreader:
    
        if row['num_pozo'] == 'num_pozo':
            #redundant header row
            pass
        else:
            uso = row['Uso del agua agregado']
            
            if row['caudal'].strip() == '':
                #sometimes there are rows w/ no caudal specified, so go to the next one and don't record this.
                continue
            else:
                caudal = Decimal(row['caudal'])
                caudal_humano = 0
                caudal_agroganaderia = 0
                caudal_industrial = 0
                caudal_turismo = 0
                caudal_otros = 0
                
                if uso == 'Consumo humano':
                    caudal_humano = caudal
                elif uso == 'Agroganadería':
                    caudal_agroganaderia = caudal
                elif uso == 'Industrial y comercial':
                    caudal_industrial = caudal
                elif uso == 'Turismo':
                    caudal_turismo = caudal
                elif uso == 'Otros':
                    caudal_otros = caudal
                
            provincia = row['provincia']
            canton = row['canton']
            distrito = row['distrito']
            
            if distrito == '0' or distrito == '-99':
                #looks like we've got some bad districts, out these wells
                continue

            if distrito in distritos:
                distritos[distrito]['caudal'] = distritos[distrito]['caudal'] + caudal
                distritos[distrito]['caudal humano'] = distritos[distrito]['caudal humano'] + caudal_humano
                distritos[distrito]['caudal agroganaderia'] = distritos[distrito]['caudal agroganaderia'] + caudal_agroganaderia
                distritos[distrito]['caudal industrial'] = distritos[distrito]['caudal industrial'] + caudal_industrial
                distritos[distrito]['caudal turismo'] = distritos[distrito]['caudal turismo'] + caudal_turismo
                distritos[distrito]['caudal otros'] = distritos[distrito]['caudal otros'] + caudal_otros
                distritos[distrito]['pozos'] = distritos[distrito]['pozos'] + 1
            else:
                distritos[distrito] = {'caudal':caudal,'caudal humano':caudal_humano,'caudal agroganaderia':caudal_agroganaderia,'caudal industrial':caudal_industrial,'caudal turismo':caudal_turismo,'caudal otros':caudal_otros,'provincia':provincia,'canton':canton,'codigo':distrito,'pozos':1}
                
    with open('output/distritos.csv','wb') as distritosfile:
        distritoswriter = csv.DictWriter(distritosfile, ['codigo','provincia','canton','caudal','caudal humano','caudal agroganaderia','caudal industrial','caudal turismo','caudal otros','pozos'])
        distritoswriter.writeheader()
        distritoswriter.writerows(distritos.values())
