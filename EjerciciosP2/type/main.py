from headlines import headline

def run(mssg:str):
    print(headline(mssg))
    print(headline(mssg,align="center"))

if __name__=='__main__':
    run("python type checking")