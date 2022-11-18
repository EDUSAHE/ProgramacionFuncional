from statistics import mean

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
    alumnas_menores = {(i[0],i[3]) for i in students if i[2]<18 and i[3]=='M'}
    aprobados = {i[0] for i in students if mean(i[1])>=6.0}

    not_aproved_students = names.difference(aprobados)

    print(names)
    print("-------------------------------------------------")
    print(names_ages)
    print("-------------------------------------------------")
    print(alumnas_menores)
    print("-------------------------------------------------")
    print(aprobados)
    print("-------------------------------------------------")
    print(not_aproved_students)

if __name__ == '__main__':
    anything()