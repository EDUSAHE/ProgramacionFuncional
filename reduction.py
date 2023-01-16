import math
#len
l = [1,2,3]
print(len(l))

r = range(3,100,3)
print(len(r))

m = map(math.sqrt,l)
print(len(list(m)))

s = 'Hello World'
print(len(s))

#sum

print(sum(l))
print(sum(r))
m = map(math.sqrt,l)
print(sum(m))
print(sum(map(math.sqrt,l),10))
# print(sum(s))

a = [[2,4],[0,0],[5,3]]
print(sum(a,[]))

l1 = [1,2,3]
l2 = [4,5,6]
lr = l1+l2
print(lr)

t1 = (1,2,3)
t2 = (4,5,6)
tr = t1+t2

r = sum(sum(a,[]))

s1 = 'abc'
s2 = 'def'
sr = s1 + s2
print(sr)

s = ['abc','def','ghi']
sr = ''.join(s)
print(sr)

#min

a = [2,5,7,1]
print(min(a))
m = map(math.sqrt,l)
print(min(m))

b = [[1,2,3],[1,1,5],[6,7,8],[1,1,4]]
print(min(b))

c = [1,2,3,4,5]
print(min(c,default=0))

from operator import itemgetter
print(min(b,default=0, key= itemgetter(1)))

#max

#any

print(any([1,0,2]))
print(any(['a','','b']))
print(any(['',0,False]))
print(any([]))
print("-------------------")

#all
print(all([1,0,2]))
print(all(['a','','b']))
print(all(['',0,False]))
print(all([]))

import functools,operator
# reduce aplica la funcion a los primeros dos elementos, posteriormente el resultado de 
# esa aplicacion lo ocupa al aplicar la funcion al tercer elemento
a = [2,3,5,2]
print(functools.reduce(operator.mul,a))

b = [2]
print(functools.reduce(lambda x,y: x*y,b,10))