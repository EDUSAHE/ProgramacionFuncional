import numpy as np

number = [1,2,3,4]
n = iter(number)

print(number[2])

try:
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))
except StopIteration:
    print("Fin del Iterador")

print("Hola")

temperatures = [12.123,11.3456,9.9999,7.897879]
b = map(round,temperatures)
print(list(b))

print(chr[97])
numb = [97,93,45,64,65]
c = map(chr,numb)
print("".join(c))

def mult(x,y,z):
    return x*y*z
t = (3,5,7)

print(mult(3,5,7))
print(mult(t))

def distEucli(x1,x2,y1,y2):
    return np.sqrt((pow((x2-x1),2)-pow((y2-y1),2)))

a = ((3,5),(4,5),(3,9))
b = ((6,9),(2,9),(0,3))

distEucli(*a)