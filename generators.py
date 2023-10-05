'''
Una funcion ocupa un espacio de memoria para guardarse y ejecutarse cada vez que sea llamada

En un generador, cada vez que se llame, el resultado devuelto se guarda en memoria 
para la proxima llamada del generador. 
Se mantiene el estado de la funcion por cada llamada
'''

def alphabet():
    for c in 'abcde':
        yield c
    
for x in alphabet():
    print(x)
print("-----------")

#Ejemplo con next
g = alphabet()
x = next(g)
print(x)
x = next(g)
print(x)
x = next(g)
print(x)
print("-----------")

#Ejemplo con fibonacci
def fibonacci():
    c = 0
    n = 1
    while True:
        yield c         #Regresa al main o a donde fue llamada
        c, n = n, c+n   #Cada vez que se llame el generador, se continua en la linea despues del yield

#para que i pueda consumir a la funcion, la convierte en iterable
for i in fibonacci():
    print(i)
    if i>100:   #Prevenir un desbordamiento
        break
print("-----------")
'''
Generador vs Iterador
    -Un generador produce un iterable
'''

def identity(it):   #funcion que se devuelve a si misma
    for x in it:
        yield x

x = range(4)    #range devuelve un ITERABLE
print(x)
print("-----------")

for i in identity(range(4)):
    print(i)
print("-----------")

#funcion para encadenar elementos de 2 iterables
def chain(it1,it2):
    for x in it1:   #devuelve los elementos de it1
        yield x     #retorna este punto cuando es llamada de nuevo
    for x in it2:   #acabando, devuelve los de it2
        yield x     #retorna este punto cuando es llamada de nuevo 

for i in chain(range(4),reversed(range(3))):
    print(i)
print("-----------")

'''
generators comprehension  ()
Ventajas:
    -Si la lista es muy grande, podemos ocupar generators para ahorrar espacio en memoria
'''
#lista con caracteres del 0 - 99
a = [str(i) for i in range(100)]    #Cuando se ejecute esta linea, se almacenan los caracteres en MEMORIA
print(a)    
print("-----------")

#con generators
a = (str(i) for i in range(100))
#No se ejecuta hasta ser requerida -> programacion perezosa
print(list(a))
print("-----------")

import math

#Instrucciones equivalentes
m = map(math.sqrt, range(100))  #con map
print(list(m))
print("-----------")
m2 = (math.sqrt(x) for x in range(100)) #con generators comprehension
print(list(m2))
print("-----------")

# m3 = map(lambda x:math.sqrt(x)+1, range(100))   #con map y lambda
# print("-----------")
# m4 = (math.sqrt(x)+1 for x in range(100))   #con generators comprehension
# print("-----------")

#filter map
l = [-1,2,7,4,-6,9,-3]
m = map(math.sqrt, filter(lambda x:x>=0, l))
#primer filtramos y luego aplicamos la 1er funcion
g = (math.sqrt(x) for x in l if x>=0)   #con generators
