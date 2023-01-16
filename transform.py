names = ('Ana','Carlos','Javier','Maria')
last_name = ('Martinez','Santos','Olivera','Hernandez')
ages = (19,21,20,19,12)
for n in names:
    print(n)

for i in range(len(names)):
    print(i+1,". ",names[i])

for n in enumerate(names):
    print(n)

for i,j in enumerate(names,1):
    print(i,". ",j)

t = (45,7)

i,j = t

for full_name in zip(names,last_name):
    print(full_name)

a = (10,11,12,13,14,15)
b = (20,21,22,23,24,25)
c = (30,31,32,33,34,35)

z = zip(a,b,c)

print(z)

#El operador estrella
restored = zip(*z)
print(list(restored))

k = [3,2,7,6,9,9,8]
r = filter(lambda x: x>7,k)

print(r)
# print(list(r))

for i in r:
    print(i)

colour = ('red','','green','','blue')
for s in filter(len,colour):
    print(s)

def square(x):
    print("Evaluacion de square")
    return x*x

a = [2,5,6]
print("Llama a map")
m = map(square,a)

print("Entra al for")
for x in m:
    print("Se inicio el cuerpo del for")
    print(x)

import operator

operator.add(5,6)

a = [20,30,40]
b = range(3)

m = map(operator.add,a,b)

print(list(m))

a = [2,4,6,8]
r = reversed(a)
print(list(r))

m = map(square,a)
r = reversed(list(m))
print(list(r))

# for i in range(9,-1,-1):
    # print(i)
# for i in reversed(range(10)):
    # print(i)

k = [1,2,3]
k.reverse()
print(k)

dates = ['2019/04/06','2017/02/11','2019/03/30','2018/01/01','2019/04/08','2017/03/02','2017/04/05','2018/06/06','2019/09/30','2018/04/11','2017/03/14']
sorted_dates = sorted(dates)
print(sorted_dates)
sorted_dates = sorted(sorted_dates, key=lambda x:x[5:7])
print(sorted_dates)
sorted_dates = sorted(sorted_dates, key=lambda x:x[0:4])
print(sorted_dates)

dates2 = [('2019','04','06'),('2017','02','11'),('2019','03','30'),('2018','01','01'),('2019','04','08'),('2017','03','02'),('2017','04','05'),('2018','06','06'),('2019','09','30'),('2018','04','11'),('2017','03','14')]

people = list(zip(names,last_name,ages))
print(people)

#Ordenar por apellido
people_sorted = sorted(people, key= lambda x: x[1])
print(people_sorted)

from operator import itemgetter
people_sorted = sorted(people, key=itemgetter(1))
print(people_sorted)
#Itemgetter tiene el mismo comportamiento que un closer
f = itemgetter(1)
t = ('Ana','Juarez',19)
s = f(t)
print(s)

fruits = ['Banana','apple','Apricot','Clementine','avocado']
sorted_fruits = sorted(fruits)
print(sorted_fruits)

sorted_fruits = sorted(fruits,key= lambda x: x.lower())
print(sorted_fruits)

from operator import methodcaller
sorted_fruits = sorted(fruits, key= methodcaller('lower'))
print(sorted_fruits)

f = methodcaller('lower')
s = f('Banana')
print(s)

import math 
k = [1,2,-2,16,-3,36,-1]
f = filter(lambda x: x >= 0, k)
m = map(math.sqrt, f)
#Utilizando composicion
m = map(math.sqrt,filter(lambda x: x >= 0, k))
print(list(m))

def same(s):
    print('Same',s)
    return s

def not_empty(s):
    if s:
        print('True', s)
        return True
    else:
        print('False')
        return False

k = ['a','','b','']
m = map(same,filter(not_empty,k))
print("Start")
for s in m:
    print("Dentro ciclo",s) #siempre  pendientes, por que el filter es muy inteligente

def format_person(first,last,age):
    return "{}, {} - age {}".format(last,first,age)

people = [('Arturo','Martinez',25),('Veronica','Juarez',19),('Maria','Lopez',26)]

print(*zip(*people))
m = map(format_person,*zip(*people))
for p in m:
    print(p)