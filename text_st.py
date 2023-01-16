new = "Mastique y tragues, tragues y mastiques Yo contigo ya no regreso Ni aunque me llores ni me supliques Yo entendí que no es culpa mía que te critiquenYo solo hago música Perdón que te sal-pique. Me dejaste de vecina a la suegra Con la prensa en la puerta y la deuda en Hacienda Te creíste que me heriste y me volviste más dura Las mujeres ya no lloran -Shak 2023"

new = new.split()
print(new)
lenghts = map(len,new)
avg = sum(lenghts)/len(new)

print(avg)

avg = sum(map(len,new))/len(new)

stop_words = ['las', 'tragues', 'no']

s = filter(lambda x: x not in stop_words, new)
s = list(s)
# avg = sum(map(len,s))/len(s)

def sumcount(it):
    sum = 0
    count = 0
    for x in it:
        sum += len(x)
        count += 1
    return sum,count

total, count = sumcount(s)
avg = total/count

s = filter(lambda x: x not in stop_words, new)
m = map(len,s)
e = enumerate(m,1)

print(tuple(e))

import functools
import operator

s = filter(lambda x: x not in stop_words, new)
m = map(len,s)
functools.reduce(operator.add,m)

def opssumcount(a,b):
    return (b[0], a[1]+b[1])

s = filter(lambda x:x not in stop_words, new)
m = map(len,s)
total,count = functools.reduce(opssumcount,enumerate(m,1))
avg = total/count
print(avg)

