import csv


def powerset(itemList):
	result = [[]]
	for item in itemList:
		newsubsets = [subset + [item] for subset in result]
		result.extend(newsubsets)
	return result

def listFromFile(csv_file):
    """
    get data from a csv file and :
    converts numbers, remove first title line
    returns a list including name, cost: int, roi: float
    """
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

def splitActions(actionList):
    """
    split list in two parts, just in case we need to divide the operation for
    more efficiency
    returns a tuple with two lists
    """
    liste1 = []
    liste2 = []
    for i in range(len(actionList)):
        if (i < 10):
            liste1.append(actionList[i])
        if (i >= 10):
            liste2.append(actionList[i])
    return (liste1, liste2)

def selectActions(actionList, max):
    """
    :param actionList: takes a list of combinations and a max
    :return: a list of selected combinations where cost is under max
    """
    best = []
    best2 = []
    for i in actionList:
        cout = 0
        rendement = 0
        for action in i:
            cout += action[1]
            rendement += action[2]
        if cout < int(max):
            best.append((rendement, cout, i))
            best2.append(i)
    return best, best2



actions = listFromFile("/home/b/Documents/OCR/projet7/actions.csv")
powerActions = powerset(actions)
selectedActions, selected = selectActions(powerActions, 500)

print("Longueur de la liste d'actions:", len(actions))
print("Nb de combinaisons:", len(powerActions))
print("Nb de combinaisons au cout inferieur à 500:", len(selectedActions))

#tri des actions sur le rendement
best_sorted = sorted(selectedActions, key=lambda k: k[0], reverse=True)
best2 = sort(selected, key=lambda k:[])
#print("\nfive last sorted :")
#for i in range(len(best_sorted)-1, len(best_sorted)-10, -1):
#    print("set", i, ":", best_sorted[i])
#print(f"Rendement: {sum(x[2][1] * x[2][2]/100 for x in best_sorted[0])}")
print(selected[1])
print("Meilleur rendement:", best_sorted[0][0], "%")
print("Actions sélectionnées:")
for action in best_sorted[0][2]:
    print(f"Nom: {action[0]}, Cout: {action[1]}, Rendement: {action[2]}%")