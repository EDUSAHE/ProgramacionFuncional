from statistics import mean
import random

"""
fruits = {'apple', 'banana', 'cherry', 'orange', 'pear'}
favorite_fruits = {'apple', 'banana', 'cherry', 'orange', 'pear', 'apple'}

print(len(fruits))

for fruit in favorite_fruits:
    print(fruit)

print('banana' in fruits)

fruits.add("blueberry")
print(fruits)
"""

def anything():
    students = (
            ('Carlos',[7.7,6.6,8.9],19,'H'),
            ('Anabell',[8.1,8.8,7.9],16,'M'),
            ('Octavio',[7.9,8.9,6.9],17,'H'),
            ('Angel',[7.9,8.9,6.9],16,'H'),
            ('Denisse',[7.9,8.9,6.9],15,'M'),
            ('Luis',[0.0,0.0,0.0],18,'H'),
            ('Diego',[0.0,0.0,0.0],17,'H'),
            ('Jesus',[0.0,0.0,0.0],16,'H'),
            ('Alejandro',[0.0,0.0,0.0],21,'H'),
            ('Julia',[0.0,0.0,0.0],21,'M'),
        )
    names = {i[0] for i in students}
    names_ages = {(i[0],i[2]) for i in students if i[2]>=18}
    aprobados = {i[0] for i in students if mean(i[1])>=6.0}
    alumnas_menores = {(i[0],i[3]) for i in students if i[2]<18 and i[3]=='M'}
    alumnas_names = {i[0] for i in students if i[3]=='M'}

    diferencia = names.difference(alumnas_names)
    print(diferencia)


"""
def run():
    x = random.randint(1,100)
    # print(x)
    students = ['Ana', 'Roberto', 'Enrique' , 'Maria']
    ages = [19,21,23,45]
    print(list(zip(students,ages)))
    dictionary = {student:age for (student,age) in zip(students,ages)}
    l = [[name,random.randint(1,10)] for name in students]
    t = tuple([(name,random.randint(1,10)) for name in students])
    d = {name:random.randint(1,10) for name in students}
    c = {(name,random.randint(1,10)) for name in students}
    print(l)
    print(t)
    print(d)
    print(c)
"""

if __name__ == '__main__':
    anything()
