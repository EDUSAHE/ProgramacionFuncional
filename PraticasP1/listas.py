from statistics import mean
def func():
        """numbers = []
        for i in range(i,11):
                numbers.append(i**2)
        """
        t = (('Carlos',[7.7,6.6,8.9],19,'H'),
             ('Anabell',[8.1,8.8,7.9],18,'M'),
             ('Octavio',[7.9,8.9,6.9],17,'H'),
             ('Angel',[7.9,8.9,6.9],16,'H'),
             ('Denisse',[7.9,8.9,6.9],21,'M'),
             ('Luis',[8.1,8.8,7.9],18,'H'),
             ('Diego',[7.9,8.9,6.9],17,'H'),
             ('Jesus',[7.9,8.9,6.9],16,'H'),
             ('Alejandro',[7.9,8.9,6.9],21,'H'),
             ('Iker',[0.0,0.0,0.0],21,'H'),
            )
        # students = [i for i in t if i[2]>=18 and i[3]=='M']
        # students = [i for i in t if (sum(i[1])/len(i[1]))>=6.0]
        # print(students)
        # numbers = [i**2 for i in range(1,10) if i%2==0]
        # print(numbers)

def listcomps():
    num = [1,2,3]
    alpha = ['a','b','c']
    l = [(x,y) for x in num for y in alpha]
    print(l)

def lista():
    numeros = [i for i in range(1,100000) if i%3==0 and i%6==0 and i%9==0 ]
    print(numeros)

def diccionario():
    my_dict = {i:i**3 for i in range(1,101) if i%3!=0}
    print(my_dict)


def diccionario2():
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
            ('Iker',[0.0,0.0,0.0],21,'H'),
        )
    dict1 = {i[0]:{"calificiones":i[1],"edad":i[2],"sexo":i[3]} for i in students}
    dict2 = {i[0]:{"calificiones":i[1],"edad":i[2],"sexo":i[3]} for i in students if i[2]>=18}
    dict3 = {i[0]:{"calificiones":i[1],"edad":i[2],"sexo":i[3]} for i in students if i[2]<18 and i[3]=='M'}
    dict4 = {i[0]:{"calificiones":i[1],"edad":i[2],"sexo":i[3]} for i in students if mean(i[1])>=6.0}
    # Genera conjunto con todos los nombres de los estudiantes
    conjunto = {i[0] for i in students}
    print(conjunto)

if __name__ == '__main__':
    diccionario2()