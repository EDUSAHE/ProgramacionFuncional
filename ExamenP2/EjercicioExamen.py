import operator,csv

def read_csv(archivo:str)->tuple:
    with open(archivo) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        data =[]
        for fila in reader:
            data.append(tuple(fila))
    return tuple(data)

if __name__ == '__main__':
    tupla = read_csv('./soccer_df3.csv')