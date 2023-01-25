import operator,csv,functools

def read_csv(archivo:str):
    with open(archivo) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data =[]
        for fila in reader:
            data.append(list(fila))
    return data

def teams_winers(datos):
    return filter(lambda x: x[5]=='H',datos)

def closer(datos):
    def compa(x):
        return {'HomeTeam':x,'Total FTHG':functools.reduce(operator.add,[int(i[3]) for i in filter(lambda y: y[1]==x,datos)]),'Total FTAG':functools.reduce(operator.add,[int(i[4]) for i in filter(lambda y: y[1]==x,datos)])}
    return compa

def goalsbyteam(datos):
    a = closer(datos)
    return map(a,{x[1] for x in datos})

def goal_percentage(datos):
    return filter(lambda x: operator.truediv(operator.mul(x['Total FTHG'],100),operator.add(x['Total FTHG'],x['Total FTAG']))>85,datos)

if __name__ == '__main__':
    lista = read_csv('./soccer_df3.csv')
    print(lista)
    ganadores_locales = list(teams_winers(lista))
    print(ganadores_locales)
    goles_equipos = list(goalsbyteam(ganadores_locales))
    print(goles_equipos)
    equipos_porcentaje = list(goal_percentage(goles_equipos))
    print(equipos_porcentaje)

