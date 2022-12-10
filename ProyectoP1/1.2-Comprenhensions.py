"""
PROGRAMACION FUNCIONAL
Sanchez Hernandez Jose Eduardo
Santibañez Garcia Luis Diego
Hernandez Rosario Christian de Jesus
"""

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

# 1. Lista que contenga los nombres de las películas que fueron estrenadas entre los años 2000 y 2015.
def Movies1(data):
    lista = [i['Movie Title'] for i in data if int(i['Year of Realease'])>=2000 and int(i['Year of Realease'])<=2015]
    return lista

# 2. Lista de tuplas, donde las tuplas están compuestas por las columnas:
# Movie Title, Movie Rating y Duration(Mins) de solo aquellas películas que su Classification sea B15.
def Movies2(data):
    lista = [(i['Movie Title'],i['Movie Rating'],i['Duration(Mins)']) for i in data if i['Classification']=='B15']
    return lista

# 3. Lista de diccionarios los cuales contienen todas columnas y todos los registros del csv que tengan un Gross (Million) mayor o igual a 20 pero menor que 78.
def Movies3(data):
    lista = [i for i in data if float(i['Gross(Million)'])>=20 and float(i['Gross(Million)'])<=78]
    return lista

# 4. Lista de tuplas, donde las tuplas están compuestas por las columnas:
#Movie Title y Genre de solo aquellas películas que su Movie Rating sea mayor o igual a 4.5.
def Movies4(data):
    lista = [(i['Movie Title'],i['Genre']) for i in data if float(i['Movie Rating'])>=4.5]
    return lista

# 5. Lista de diccionarios con todos los registros y con las columnas:
#Movie Title, Year of Realease, Movie Rating y Duration (Mins) que estén dentro del género Horror.
def Movies5(data):
    lista = [{'Movie Title':i['Movie Title'],'Year of Realease':i['Year of Realease'],'Movie Rating':i['Movie Rating'],'Duration(Mins)':i['Duration(Mins)']} for i in data if ('Horror' in i['Genre'])==True]
    return lista


# 6. Diccionario con todos los registros y columnas donde Movie Rating > 8.5 y Duration < 140
def Movies6(data):
    diccionario = {i['Movie Title']: {'Year of Realease': i['Year of Realease'],
                                    'Genre': i['Genre'], 'Movie Rating': i['Movie Rating'], 'Duration(Mins)': i['Duration(Mins)'],
                                    'Gross(Million)': i['Gross(Million)'], 'Classification': i['Classification']} for i in data
                 if i['Movie Rating'] > '8.5' and i['Duration(Mins)'] < '140'}
    return diccionario


# 7. Diccionario con las columnas Movie Title, Year of Release , Genre, y Duration(Mins)
# donde Genre="Action,Adventure,Sci-Fi" y hayan salido despues del año 2000
def Movies7(data):
    diccionario = {i['Movie Title']: {'Year of Realease': i['Year of Realease'],
                                    'Genre': i['Genre'], 'Duration(Mins)': i['Duration(Mins)'], } for i in data
                 if i['Genre'] == "Action,Adventure,Sci-Fi" and i['Year of Realease'] >= '1998'}
    return diccionario

# 8. Diccionario con las columnas Genre, Movie Title, Movie Rating , Year of Realease , Classification
# donde Movie Rating sea mayor a 8 y la Classification no sea B ni A
def Movies8(data):
    diccionario = {i['Genre']: {'Movie Title': i['Movie Title'],
                              'Movie Rating': i['Movie Rating'], 'Year of Realease': i['Year of Realease']} for i in data
                 if i['Movie Rating'] >= '8' and i['Classification'] != "B" and i['Classification'] != "A"}
    return diccionario


# 9. Diccionario con las columnas Movie Title, Classification Year of Realease,Genre y Duration(Mins)
# donde las diccionario hayan salido antes de 1990, la clasifiacion sea A y dure menos de 150 minutos
def Movies9(data):
    diccionario = {i['Movie Title']: {'Year of Realease': i['Year of Realease'], 'Classification': i['Classification'],
                                    'Genre': i['Genre'], 'Duration(Mins)': i['Duration(Mins)']} for i in data
                 if i['Year of Realease'] <= "1990" and i['Classification'] == "A" and i['Duration(Mins)'] < '150'}
    return diccionario

# 10. Diccionario con las columnas Movie Title, Classification, Year of Realease,Genre
# donde La pelicula comience con The y el genero sea Action,Adventure,Sci-Fi
def Movies10(data):
    diccionario = {i['Movie Title']: {'Year of Realease': i['Year of Realease'], 'Classification': i['Classification'],
                                    'Genre': i['Genre']} for i in data
                 if i['Movie Title'].startswith('The') and i['Genre'] == 'Action,Adventure,Sci-Fi'}
    return diccionario

# 11. Conjunto de tuplas (nombre,año) de todas las peliculas donde el año sea menor a 2000
def Movies11(data):
    set11 = {(i['Movie Title'],i['Year of Realease']) for i in data if i['Year of Realease']<'2000'}
    return set11

# 12. Conjunto de tuplas (nombre,clasificacion) de todas las peliculas que no sean clasificacion 'A' o 'AA'
def Movies12(data):
    set12 = {(i['Movie Title'],i['Classification']) for i in data if (i['Classification']!='A' and i['Classification']!='AA')}
    return set12

# 13. Conjunto de tuplas (nombre,año) de todas las peliculas donde el año este entre 1990-2010
def Movies13(data):
    set13 = {(i['Movie Title'],i['Year of Realease']) for i in data if (i['Year of Realease']>='1990' and i['Year of Realease']<='2010')}
    return set13

# 14. Conjunto de tuplas (nombre,genero,duracion) de todas las peliculas donde el genero sea Action,Adventure,Fantasy y su duracion mayor o igual a 100
def Movies14(data):
    set14 = {(i['Movie Title'],i['Genre'],i['Duration(Mins)']) for i in data if i['Genre']=="Action,Adventure,Fantasy" and int(i['Duration(Mins)'])>=100}
    return set14

# 15. Conjunto del nombre de todas las peliculas donde el genero sea diferente a Action,Adventure,Fantasy
def Movies15(data):
    set15 = {i['Movie Title'] for i in data if i['Genre']!="Action,Adventure,Fantasy"}
    return set15

# 16. Conjunto resultante de la UNIÓN de los conjuntos 11 y 13.
def Movies16(data):
    setA = Movies11(data)
    setB = Movies13(data)
    set16 = setA.union(setB)
    return set16

# 17. Conjunto resultante de la UNIÓN del conjunto 15 con el conjunto de los Movie Titles obtenido del conjunto 14.
def Movies17(data):
    set15 = {i['Movie Title']
             for i in data if i['Genre'] != "Action,Adventure,Fantasy"}
    set14 = {i['Movie Title']  for i in data if i['Genre']
             == "Action,Adventure,Fantasy" and int(i['Duration(Mins)']) >= 100}
    set17 = set15.union(set14)
    return set17

# 18. Conjunto resultante de la INTERSECCIÓN del conjunto 11 con el conjunto de los Movie Titles obtenidos del conjunto 13.
def Movies18(data):
    set11 = {i['Movie Title']
             for i in data if i['Year of Realease'] < '2000'}
    set13 = {i['Movie Title'] for i in data if (
        i['Year of Realease'] >= '1990' and i['Year of Realease'] <= '2010')}
    set18 = set11.intersection(set13)
    return set18

# 19. Conjunto resultante de la INTERSECCIÓN de todas las películas realizadas después del año 2000  y de todas las películas con Movie Rating mayor a 8, donde los elementos sean una tupla (Movie Titles, Year Released, Movie Rating). def Movies19(data):
def Movies19(data):
    setA = {(i['Movie Title'],i['Year of Realease'],i['Movie Rating']) for i in data if i['Year of Realease']>'2000'}
    setB = {(i['Movie Title'],i['Year of Realease'],i['Movie Rating']) for i in data if i['Movie Rating']>'8'}
    set19 = setA.intersection(setB)
    return set19

# 20. Conjunto resultante de la diferencia de un conjunto de películas realizadas después del año 2010 con un conjunto de películas de clasificación ‘A’.
def Movies20(data):
    set20 = {i['Movie Title'] for i in data if i['Year of Realease'] > '2010'}
    set21 = {i['Movie Title'] for i in data if i['Classification'] == "A"}
    set22 = set20.difference(set21)
    return set22

if __name__ == '__main__':
    peliculas = read_csv()
    print(Movies1(peliculas))
    print(Movies2(peliculas))
    print(Movies3(peliculas))
    print(Movies4(peliculas))
    print(Movies5(peliculas))
    print(Movies6(peliculas))
    print(Movies7(peliculas))
    print(Movies8(peliculas))
    print(Movies9(peliculas))
    print(Movies10(peliculas))
    print(Movies11(peliculas))
    print(Movies12(peliculas))
    print(Movies13(peliculas))
    print(Movies14(peliculas))
    print(Movies15(peliculas))
    print(Movies16(peliculas))
    print(Movies17(peliculas))
    print(Movies18(peliculas))
    print(Movies19(peliculas))
    print(Movies20(peliculas))