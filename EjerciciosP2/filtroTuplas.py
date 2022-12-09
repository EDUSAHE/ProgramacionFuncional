

def filtros(n):
    def filtrado(tupla):
        return tuple([i for i in tupla if i[3]==n])
    return filtrado

def addpromedio():
    def addcampo(tupla):
        return tupla([])
    

if __name__ == '__main__':
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
            ('Julia',[0.0,0.0,0.0],21,'M')
        )

    f1 = filtros('M')
    print(f1(students))