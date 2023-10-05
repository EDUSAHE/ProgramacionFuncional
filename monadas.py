#functor
from oslash import Just,Nothing,List
from operator import neg,add

a = Just(3) #a se convierte en un envoltorio para verlo como una funcion
print(a)

print(neg(4))

b = a.map(neg)
b = neg % a
print(b)

n = Nothing()
print(n)

nn = neg % n
print(nn)

l = List.from_iterable([1,2,3,4,5,6,7])
print(l)
print(type(l))

ln = l.map(neg)
print(ln)

#Functors Aplicativos

a = Just(3)
f = Just(neg)
b = f.apply(a)
# b = a * f #Aplicar Funcion f a a

a = Just(2)
b = add % a

print(b)