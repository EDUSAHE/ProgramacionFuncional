def convert(values, f):
    return f(values)


def miles_2_kilo(miles):
    return miles * 1.60934


def inche_2_cm(inches):
    return inches * 2.54


def feet_2_cm(feet):
    return feet * 30.48


def yard_2_cm(yard):
    return yard * 91.44


def run():
    menu = """
    1. Millas a kilometros
    2. Pulgadas a centimetros
    3. Pies a centimetros
    4. Yardas a centimetros
    """
    print(menu)
    option = int(input(
        "Introdusca el numero correspondiente a el tipo de conversion que desea:  "))
    if option==1:
        m = float(input("Millas a convertir: "))
        print(f"{m} Millas son {convert(m,miles_2_kilo)} Kilometros")
    elif option==2:
        m = float(input("Pulgadas a convertir: "))
        print(f"{m} Pulgadas son {convert(m,inche_2_cm)} centimetros")
    elif option==3:
        m = float(input("Pies a convertir: "))
        print(f"{m} Pies son {convert(m,feet_2_cm)} centimetros")
    elif option==4:
        m = float(input("Yardas a convertir: "))
        print(f"{m} Yardas son {convert(m,yard_2_cm)} centimetros")
    else:
        print('error conversion no disponible')

if __name__ == '__main__':
    run()
