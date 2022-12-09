def codestr(c):
    return(hex(ord(c)))

def compose(f,g):
    def fn(x):
        return f(g(x))
    return fn

if __name__ == '__main__':
    h = codestr('x')
    print(h)

    codestr2 = compose(hex,ord)