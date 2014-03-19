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
                
            provincia = row['provincia']
            canton = row['canton']
            distrito = row['distrito']
            
            if distrito == '0' or distrito == '-99':
                #looks like we've got some bad districts, out these wells
                continue

            if distrito in distritos:
                distritos[distrito]['caudal'] = distritos[distrito]['caudal'] + caudal
                distritos[distrito]['pozos'] = distritos[distrito]['pozos'] + 1
            else:
                distritos[distrito] = {'caudal':caudal,'provincia':provincia,'canton':canton,'codigo':distrito,'pozos':1}
                
    with open('output/distritos.csv','wb') as distritosfile:
        distritoswriter = csv.DictWriter(distritosfile, ['codigo','provincia','canton','caudal','pozos'])
        distritoswriter.writeheader()
        distritoswriter.writerows(distritos.values())
