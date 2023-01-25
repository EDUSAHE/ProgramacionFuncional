def maxn(n):
    def f(x):
        return max(n,x)
    return f

max0 = maxn(0)
print(max0(3))
print(max0(-1))
print("********************")

def max0(x):
    return max(0,x)

map(lambda x: max(0,x),(1,-3,5,-7))

m = map(maxn(3),[1,2,3,4,5])

def quad(a,b,c,x):
    return a*x*x + b*x + c

def quad_abc(a,b,c):
    def f(x):
        return quad(a,b,c,x)
    return f

my_quad = quad_abc(1,-3,2)
print(my_quad(0))
print(my_quad(1))
print(my_quad(2))


def quad_ab(a,b):
    def f(c,x):
        return quad(a,b,c,x)
    return f

my_quad2 = quad_ab(1,-3)
print(my_quad2(2,0))
print(my_quad2(2,1))
print(my_quad2(2,2))

from functools import partial

max0 = partial(max,0)
print(max0(2))
print(max0(-1))

m = map(partial(max,0),[1,2,-3,4,-5])

quad3 = partial(quad,1,-3,2)
print(quad3(0))
print(quad3(1))
print(quad3(3))

quad2 = partial(quad,1,-3)
print(quad2(2,0))
print(quad2(2,1))
print(quad2(2,3))

def quad_ac(a,c):
    def f(b,x):
        return quad(a,b,c,x)
    return f

def make_print(sep):
    def f(*args):
        return print(*args,sep=sep)
    return f

print_csv = make_print(", ")
print_csv(1,2,3)

print_colon = make_print(": ")
print_colon(1,2,3)

