import csv

def listFromFile(csv_file):
    liste = []
    with open(csv_file) as file:
        data = csv.reader(file)
        for i in data:
            liste.append(i)
    liste.pop(0)
    for item in liste:
        item[1] = int(item[1])
        item[2] = float(item[2].strip("%"))

    return liste

def listFromFile2(csv_file):
    liste = []
    with open(csv_file) as file:
        data = csv.reader(file)
        for i in data:
            liste.append(i)
    liste.pop(0)
    for item in liste:
        item[1] = float(item[1])
        item[2] = float(item[2])
    return liste

def splitListe(liste):
    liste1 = []
    liste2 = []

    for i in range(len(liste)):
        if (i < 10):
            print(liste[i])
            liste1.append(liste[i])
        if (i >= 10):
            liste2.append(liste[i])


