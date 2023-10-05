import re
import itertools

def read_file():
    with open("AlfaMasMenos5000.txt", encoding="utf8") as textfile:
        return [re.sub(r'[0-9=\n]','',i).split(',') for i in textfile if re.sub(r'[0-9=\n]','',i)]

def write_file(name,string):
    with open(name,"w", encoding="utf8") as textfile:
        textfile.write(string)
        textfile.close()
        return

def make_ngrama(data,n):
    return [",".join(data[i:n+i]) for i in range(len(data)-(n-1)) if n<=len(data)]

def count_ngramas(data,n,b,name):
    ngramas = list(itertools.chain(*map(lambda x: make_ngrama(x,n),data)))
    h = sorted(filter(lambda f: f[0]>=b,([ngramas.count(i),i] for i in {c for c in ngramas})), key=lambda x: x[0],reverse=True)
    s = "\n".join(f"[{i[0]}] {i[1]}" for i in h)
    output = f"""Se encontraron {len(h)} gramas de tamaño {n}
{s}
    """
    write_file(name,output)
    return

if __name__ == '__main__':
    l = read_file()
    count_ngramas(l,1,10,"Prueba_n_1_B_10.txt")
    count_ngramas(l,2,7,"Prueba_n_2_B_7.txt")
    count_ngramas(l,3,4,"Prueba_n_3_B_4.txt")