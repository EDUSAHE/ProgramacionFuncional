import time

def HanoiIterativo():
    

def HanoiRecursivo(n,Origen,Destino,Auxiliar):
    if n == 1:
        print(f'Disco 1 de {Origen} a {Destino}')
        return
    HanoiRecursivo(n-1,Origen,Auxiliar,Destino)
    print(f'Disco {n} de {Origen} a {Destino}')
    HanoiRecursivo(n-1,Auxiliar,Destino,Origen)
    




if __name__ == '__main__':
    start_time = time.process_time()
    HanoiRecursivo(8,'A','B','C')
    end_time = time.process_time()
    print(end_time - start_time)