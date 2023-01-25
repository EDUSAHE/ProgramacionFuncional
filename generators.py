
def alphabet():
    for c in 'abcde':
        yield c


for x in alphabet():  # cada vez que el for solicita
    print(x)

print()

g = alphabet()
x = next(g)
print(x)
x = next(g)
print(x)

print()


def fibonacci():  # generador produce un iterable
    c = 0
    n = 1
    while True:
        yield c
        c, n = n, c + n  # asignacion simultanea para ahorrar auxiliar


for i in fibonacci():
    print(i)
    if i > 100:  # pata evitar desbordamineto
        break

print()


def identity(it):
    for x in it:
        yield x


# range es iterable
for i in identity(range(4)):
    print(i)
    
print()

def chain(it1, it2):            #retoma el punto del yield
    for x in it1:
        yield x
    for x in it2:
        yield x

for i in chain(range(4), reversed(range(3))):
    print(i)



#GENERATORS COMPREHENSION

a = [str(1) for i in range(100)]         #convierte en string, en ese momento ocupa espacio en memoria

a = (str(1) for i in range(100))         #el generator usa evalcuion perezosa

import math

m = map(math.sqrt, range(100))
m = map(lambda x: math.sqrt(x) + 1, range(100))         #sumandole 1


m2 = (math.sqrt(x) for x in range(100))       #generator
m2 = (math.sqrt(x) + 1  for x in range(100))  


# filter map

l = [-1, 2, 7,4 ,-6,9 ,-3]
m = map(math.sqrt, filter(lambda x: x>= 0,l) )
print(list(m))

print()

#ahora el mismo pero generator
g = (math.sqrt(x) for x in l if x>= 0) 
print(list(g))
