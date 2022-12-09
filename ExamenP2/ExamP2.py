import csv
from statistics import mean

def read_csv():
    with open('./soccer_df.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data.append({key: value for key, value in iterable})
    return data

print(read_csv())

