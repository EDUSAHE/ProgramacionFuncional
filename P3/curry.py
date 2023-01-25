import pymonad.tools
from pymonad.reader import Compose
from functools import partial,reduce
from operator import add,mul

def compose2(f,g):
    def fn(x):
        return f(g(x))
    return fn

@pymonad.tools.curry(4)
def quadc(a,b,c,x):
    return a*x*x + b*x + c
def quad(a,b,c,x):
    return a*x*x + b*x + c
def quad_ab(a,b):
    def f(c,x):
        return quad(a,b,c,x)
    return f


y = quadc(1,-3,2,0)
f = quadc(1,-3)

y = f(2,0)

a = 1
b = 2
c = [1,2,3,4,5]
x = [2,4,5,8,10]

#currificacion con pymonads
m = map(quadc(a,b),c,x)
#aplicacion parcial con partial de functools
m = map(partial(quad,a,b),c,x)
#aplicacion parcial con closure
m = map(quad_ab(a,b),c,x)

#Composicion
x= 5
#Opcion 1
add(2,mul(3,x))

f = partial(add,2)
g = partial(mul,3)
#Opcion 2
f(g(x))
#Opcion 3
addmul1 = partial(add,2)(partial(mul,3)(x))
#Opcion 4
addmul2 = compose2(partial(add,2),partial(mul,3))



for i in reversed(range(10)):
    print(i)

countdown = compose2(reversed,range)
for i in countdown(10):
    print(i)

# p(q(r(s(x))))
# f = compose2(p,q)
# g = compose2(f,r)
# h = compose2(g,s)
# h(x)

# Como texto letras son numeros y compse es una suma 
# (((p + q) + r) + s)

l = [1,2,3,4,5]

def compose(*f):
    def compose2(f,g):
        def fn(x):
            return f(g(x))
        return fn
    return reduce(compose2,f, lambda x: x)
#Queda tarea probar compose
test = []

#Composicion de funciones con PyMonad

@pymonad.tools.curry(1)
def reversedc(x):
    return reversed(x)
@pymonad.tools.curry(1)
def rangec(x):
    return range(x)

countdown = Compose(range).then(reversed)

for i in countdown(7):
    print(i)

countdown2 = Compose(rangec).then(reversedc)

for i in countdown2(7):
    print(i)