from statistics import mean

def run():

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

    print("-----------------------------------------------")
    print(dict1)
    print("-----------------------------------------------")
    print(dict2)
    print("-----------------------------------------------")
    print(dict3)
    print("-----------------------------------------------")
    print(dict4)

if __name__ == '__main__':
    run()