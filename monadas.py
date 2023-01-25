#functor
from oslash import Just,Nothing,List
from operator import neg

a = Just(3) #a se convierte en un envoltorio
print(a)

print(neg(4))

b = a.map(neg)
b = neg % a
print(b)

n = Nothing()
print(n)

nn = neg % n
print(nn)

l = List[1,2,3]
print(l)
print(type(l))

ln = neg % l
print(ln)