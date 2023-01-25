import json
import re
import operator,functools

def read_json():
    with open("News_Category_Dataset_v3.json") as jsonFile:
        jsonObject = json.load(jsonFile)
    return [i['short_description'] for i in jsonObject]

def read_stopwords():
    with open("stopwords-en.txt", encoding="utf8") as textfile:
        data = [i.replace('\n','') for i in textfile]
    return data

def avg_words(datos,stop_words):
    total_words = " ".join(datos)
    total_words_lower = total_words.lower()
    separate_words = total_words_lower.split()
    m = map(lambda x: re.sub(r'[^a-z0-9]','',x),separate_words)
    leaked_words = filter(lambda x: x not in stop_words, list(m))
    final_words = " ".join(list(leaked_words)).split()
    tam_words = list(map(len,final_words))
    return operator.truediv(functools.reduce(operator.add,tam_words),len(tam_words))

if __name__ == '__main__':
    l = read_json()
    a = read_stopwords()
    z = avg_words(l,a)
    print(z)