import math
import functools
import operator

def factorial(x):
    return functools.reduce(operator.mul,range(1,x+1),1)

def haversine(p1,p2):
    lat_1,lon_1 = p1
    lat_2,lon_2 = p2
    d_lat = math.radians(lat_2 - lat_1)
    d_lon = math.radians(lon_2 - lon_1)
    lat_1 = math.radians(lat_1)
    lat_2 = math.radians(lat_2)
    a = math.sqrt(math.sin(d_lat/2)**2 + math.cos(lat_1)*math.cos(lat_2)*math.sin(d_lon/2)**2)
    c = 2*math.asin(a)
    return 3440*c

data = (('37.64901619777347','-76.330295186590480'),('37.840832','-76.27383399999999'),('38.331501','-76.459503'),('38.843334','-76.298668'),('37.549','-76.331169'),('38.330166','-76.458504'),('38.976334','-76.47350299999999'))

def generator(x):
    while True:
        cor1 = x
        yield
        dist = haversine(cor1,x)
        yield dist

data = list(map(lambda x: list(map(float,x)),list(data)))

