import csv

def read_csv(archivo:str)->tuple:
    with open(archivo) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data =[]
        for fila in reader:
            data.append(tuple(fila))
    return tuple(data)

def point3(datos:tuple)->tuple:
    lista = [i for i in list(datos) if i[5][0]=='H']
    return tuple(lista)

def point4(datos:tuple)->list:
    conjunto = {i[1] for i in list(datos)}
    lista = []
    d = {}
    for i in conjunto:
        d['HomeTeam'] = i
        sum1=0
        sum2=0
        for j in list(datos):
            if i==j[1]:
                sum1 += int(j[3])
                sum2 += int(j[4])
        d['Total FTHG'] = sum1
        d['Total FTAG'] = sum2
        lista.append(dict(d))
    return lista


if __name__ == '__main__':
    tupla = read_csv('./soccer_df3.csv')
    tupla2 = point3(tupla)
    lista = point4(tupla2)
    print(lista)




