class Taylor(x):
    def __init__(self) -> None:
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.c
        # Asignacion simultanea
        self.c,self.n = self.n, self.c + self.n
        return result

f = Taylor()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for i in Fibonacci():
    print(i)
    if i>1000:
        break
