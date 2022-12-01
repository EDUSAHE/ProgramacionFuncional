


def sumatoria(x):
    if x == []:
        return 0
    if isinstance(x[0],list):
        return sumatoria(x[0]) + sumatoria(x[1:]) 
    return x[0] + sumatoria(x[1:])


if __name__ == '__main__':
    lista = [1,2,[3,4],5,[[6,7],[8,9]]]
    print(sumatoria(lista))

