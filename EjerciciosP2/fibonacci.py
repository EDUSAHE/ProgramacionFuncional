from functools import lru_cache
import sys

@lru_cache(maxsize=128)
def fibonacci(n:int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
    
if __name__ == '__main__':
    
    print(sys.getrecursionlimit())
    x = int(input("Ingrese un numero: "))
    print(fibonacci(x))