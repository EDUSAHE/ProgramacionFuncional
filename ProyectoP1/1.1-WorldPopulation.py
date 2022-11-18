import csv
from statistics import mean

def read_csv():
    with open('./world_population.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data.append({key: value for key, value in iterable})
    return data

def point1(data):
    lista = [i for i in data]
    return lista

def point2(data):
    lista = [{'Rank': i['Rank'], 'CCA3': i['CCA3'],'Country/Territory': i['Country/Territory'], 'Capital': i['Capital'],'Continent': i['Continent'], 'Population': [i['2022 Population'],i['2020 Population'], i['2015 Population'],i['2010 Population'], i['2000 Population'],i['1990 Population'], i['1980 Population'],i['1970 Population']], 'Area (km²)': i['Area (kmÂ²)'],'Density (per km²)': i['Density (per kmÂ²)'], 'Growth Rate': i['Growth Rate'],'World Population Percentage': i['World Population Percentage']} for i in data]
    return lista

def point3(data):
    lista = [{'Country/Territory':i['Country/Territory'],'2022 Population':int(i['2022 Population'])} for i in data]
    return lista

def point4(data):
    lista = [(i['CCA3'],float(i['World Population Percentage'])) for i in data if float(i['World Population Percentage'])>=1.0]
    return lista

def point5(data):
    lista = [(i['CCA3'],mean([int(i['2022 Population']),int(i['2020 Population']),int(i['2015 Population']),int(i['2010 Population']),int(i['2000 Population']),int(i['1990 Population']),int(i['1980 Population']),int(i['1970 Population'])])) for i in data]
    return lista

def point6(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data}
    return conjunto

def point7(data):
    conjunto = {i['Continent'] for i in data}
    return conjunto

def point8(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='North America'}
    return conjunto

def point9(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='South America'}
    return conjunto

def point10(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='Oceania'}
    return conjunto

def point11(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='Europe'}
    return conjunto

def point12(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='Asia'}
    return conjunto

def point13(data):
    conjunto = {(i['Country/Territory'],i['Continent']) for i in data if i['Continent']=='Africa'}
    return conjunto

def point14(data):
    Europa = point11(data)
    Asia = point12(data)
    Africa = point13(data)
    union = (Europa.union(Asia)).union(Africa)
    return union

def point15(data):
    NorteA = point8(data)
    SurA = point9(data)
    union = NorteA.union(SurA)
    return union

def point16(data):
    conjunto = {(i['Country/Territory'],float(i['World Population Percentage'])) for i in data if float(i['World Population Percentage'])<0.4}
    return conjunto

def point17(data):
    conjunto = {(i['Country/Territory'],float(i['World Population Percentage'])) for i in data if float(i['World Population Percentage'])>0.2}
    return conjunto

def point18(data):
    Conjunto1 = point16(data) 
    Conjunto2 = point17(data)
    union = Conjunto1.union(Conjunto2)
    return union

def point19(data):
    Conjunto1 = point16(data) 
    Conjunto2 = point17(data)
    diferencia = Conjunto1.difference(Conjunto2)
    return diferencia

def point20(data):
    Conjunto1 = point16(data) 
    Conjunto2 = point17(data)
    diferencia = Conjunto2.difference(Conjunto1)
    return diferencia

if __name__ == '__main__':
    datos = read_csv()
    print(point1(datos))
    print(point2(datos))
    print(point3(datos))
    print(point4(datos))
    print(point5(datos))
    print(point6(datos))
    print(point7(datos))
    print(point8(datos))
    print(point9(datos))
    print(point10(datos))
    print(point11(datos))
    print(point12(datos))
    print(point13(datos))
    print(point14(datos))
    print(point15(datos))
    print(point16(datos))
    print(point17(datos))
    print(point18(datos))
    print(point19(datos))
    print(point20(datos))