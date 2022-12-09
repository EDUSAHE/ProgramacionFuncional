def potencia(n):
    def expo(base):
        print(base**n)
    return expo

def addn(n):
    def add(x):
        return x + n
    return add

if __name__ == '__main__':
    potencia_2 = potencia(2)
    potencia_2(8)

    a = [2.2,5.6,1.9,0.1]
    b = map(round,a)
    print(list(b))

    c = map(lambda x: x+1,a)
    print(list(c))

    d = map(addn(1),a)
    print(list(d))