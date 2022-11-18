import csv

with open('users.csv') as csvfile:
    users = csv.reader(csvfile,delimiter=',')
    h = next(users)

    lista = [{clave:valor for clave,valor in zip(h,datos)} for datos in users if int(datos[h.index("edad")])>=18 and int(datos[h.index("edad")])<=42 and int(datos[h.index("ocup")])%2!=0]
    lista2 = [(valor[h.index['id']],valor[h.index['edad']]) for valor in users if int(valor[h.index['cp']])<=11000 and int(valor[h.index['cp']])>=6300]

    c3 = {tuple(valor) for valor in users if valor[h.index['genero']]=='F'}

with open('users.csv') as csvfile:
    users = csv.reader(csvfile,delimiter=',')
    h = next(users)

    c4 = {tuple(valor)for valor in users if int(h.index["edad"])>=18 and int(valor[h.index["edad"]])<=23}

    x = c3.intersection(c4)
    