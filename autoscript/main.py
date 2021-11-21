import csv

file = open("Translation request for FEGtrack.csv", mode="r", encoding="utf-8")
reader = csv.reader(file, delimiter=',', quotechar='|')

for row in reader:
    if row[0] == '"Zeitstempel"':
        continue
    """
    
    """
    print(row)
