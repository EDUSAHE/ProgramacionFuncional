from statistics import mean

def mean2(students): #Calcular promedio, recibiendo una lista de estudiantes
    avg_list = []
    for i in students:
        for j in i[1]: 
            sum += j
        avg = sum/len(i[1])
        avg_list.append(avg)
    return avg_list

#LA 3 FUNCIONA CON LAMBDA, LAS DEMAS NO
def mean3(student): #Recibiendo un estudiante
    sum = 0
    for i in student[1]:
        sum += i
    avg = sum/len(student[1])
    return avg

def mean4(grades):  #Recibe calificaciones
    for i in grades:
        sum += i
    avg = sum/len(grades)
    return avg

t = (('Carlos',[7.7,6.6,8.9],19,'H'),
     ('Anabel',[8.1,8.8,7.9],18,'M'),
     ('Octavio',[7.9,8.9,6.9],17,'H'),
     ('Angel',[7.9,8.9,6.9],16,'H'),
     ('Denisse',[7.9,8.9,6.9],21,'M'),
     ('Ana',[8.1,8.8,7.9],17,'M'))

#Crear lista de tuplas
list1 = [i for i in t]
print(list1)
print("---------------")
#Ordenar nombre ASCENDENTE
student_by_name = sorted(list1)
print(student_by_name)
print("---------------")
#Ordenas nombres DESCENDETE
student_by_name = sorted(list1,reverse=True)
print(student_by_name)
print("---------------")
#Ordenar promedio ASCENDENTE
student_by_name = sorted(list1,key = lambda x : mean(x[1]))
print(student_by_name)
#O aplicando a mena3
student_by_name = sorted(list1,key = lambda x : mean3)
print(student_by_name)
#Ordenas edad DESCENDENTE
student_by_name

