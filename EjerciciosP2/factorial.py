import sys
def factorial(n:int) -> int:
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    print(sys.getrecursionlimit())
    x = int(input("Ingrese un numero: "))
    print(factorial(x))