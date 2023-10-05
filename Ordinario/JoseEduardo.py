import operator,functools


class Fibonacci():
    def __init__(self) -> None:
        self.c = 0
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.c
        self.c,self.n = self.n, self.c + self.n
        return result

f = Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


def impares(n):
    for x in range(1,n+1):
        if x%2!=0:
            yield x

i = impares(10)
print(list(i))

def convert(text):
    x=''
    for c in text:
        if (c=='	' or c=='\n') and x!='':
            yield int(x)
            x=''
        else:
            x+=c
        

text = """	2	3	5	7	11	13	17	19	23	29
31	37	41	43	47	53	59	61	67	71
73	79	83	89	97	101	103	107	109	113
127	131	137	139	149	151	157	163	167	173
179	181	191	193	197	199	211	223	227	229"""
z = convert(text)
print(list(z))


a = {s for s in range(11) if ((s>=0 and s<=10) and (s%3==0 or s%5==0))}
print(a)

def elecciones():
    data = ((194, 48, 206, 45), (180, 20, 320, 16), (221, 90, 140, 20), (432, 50, 821, 14), (820, 61, 946, 18))

    print(f"""Distrito    Candidato A     Candidato B     Candidato C     Candidato D
    1           {data[0][0]}              {data[0][1]}            {data[0][2]}              {data[0][3]}
    2           {data[1][0]}              {data[1][1]}            {data[1][2]}              {data[1][3]}
    3           {data[2][0]}              {data[2][1]}            {data[2][2]}              {data[2][3]}
    4           {data[3][0]}              {data[3][1]}            {data[3][2]}              {data[3][3]}
    5           {data[4][0]}              {data[4][1]}            {data[4][2]}              {data[4][3]}""")
    print(f"""
Candidato A 
Total de votos: {data[0][0]+data[1][0]+data[2][0]+data[3][0]+data[4][0]}
Porcentaje Votos: {((data[0][0]+data[1][0]+data[2][0]+data[3][0]+data[4][0])/(functools.reduce(operator.add,map(lambda x: functools.reduce(operator.add,x),data))))*100}
Candidato B 
Total de votos: {data[0][1]+data[1][1]+data[2][1]+data[3][1]+data[4][1]}
Porcentaje Votos: {((data[0][1]+data[1][1]+data[2][1]+data[3][1]+data[4][1])/(functools.reduce(operator.add,map(lambda x: functools.reduce(operator.add,x),data))))*100}
Candidato C 
Total de votos: {data[0][2]+data[1][2]+data[2][2]+data[3][2]+data[4][2]}
Porcentaje Votos: {((data[0][2]+data[1][2]+data[2][2]+data[3][2]+data[4][2])/(functools.reduce(operator.add,map(lambda x: functools.reduce(operator.add,x),data))))*100}
Candidato D 
Total de votos: {data[0][3]+data[1][3]+data[2][3]+data[3][3]+data[4][3]}
Porcentaje Votos: {((data[0][3]+data[1][3]+data[2][3]+data[3][3]+data[4][3])/(functools.reduce(operator.add,map(lambda x: functools.reduce(operator.add,x),data))))*100}
Candidato mas Votado: Candidato C
""")
    return

elecciones()