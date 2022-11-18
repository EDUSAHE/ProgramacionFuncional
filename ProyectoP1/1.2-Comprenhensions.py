import csv
from statistics import mean

def read_csv():
    with open('./Movies.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data.append({key: value for key, value in iterable})
    return data

def Movies1(data):
    lista = [i['Movie Title'] for i in data if int(i['Year of Realease'])>=2000 and int(i['Year of Realease'])<=2015]
    return lista

def Movies2(data):
    lista = [(i['Movie Title'],i['Movie Rating'],i['Duration(Mins)']) for i in data if i['Classification']=='B15']
    return lista

def Movies3(data):
    lista = [i for i in data if float(i['Gross(Million)'])>=20 and float(i['Gross(Million)'])<=78]
    return lista

def Movies4(data):
    lista = [(i['Movie Title'],i['Genre']) for i in data if float(i['Movie Rating'])>=4.5]
    return lista

def Movies5(data):
    lista = [{'Movie Title':i['Movie Title'],'Year of Realease':i['Year of Realease'],'Movie Rating':i['Movie Rating'],'Duration(Mins)':i['Duration(Mins)']} for i in data if ('Horror' in i['Genre'])==True]
    return lista

if __name__ == '__main__':
    peliculas = read_csv()
    print(Movies5(peliculas))