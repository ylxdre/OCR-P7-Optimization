import csv


def listFromFile(csv_file):
    """
    Extract and format data from file(csv)
    :param csv_file: full path
    :return: a list of items
    """
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

def transformData(dataset):
    """
    Transform in a list of dict with computed values as gain, ratio
    Sorted by gain
    :param dataset: list of items
    :return: a sorted list of dict
    """
    tmpset = [{'nom': x[0], 'cout': x[1],
                   'rendement': x[2],
                   'gain': x[1] * x[2] / 100,
                   'ratio1': x[2] / x[1],
                   'ratio2': (x[1] * x[2] / 100) / x[1]} for x in dataset if
                  x[1] > 0.0 and x[2] > 0.0]

    return sorted(tmpset, key=lambda x: x['gain'], reverse=True)

def sacADosFloat(actions, maximum_cost):
    """
    Use dynamic approach
    :param actions: a list of dict with minimum key as cost and gain
    :param maximum_cost: the constraint, our max cost
    :return: maximum gain: int, selected items: list
    """
    n = len(actions)
    table = [[0.0 for x in range(int(maximum_cost) + 1)] for x in range(n + 1)]

    # Dynamic programing table
    for i in range(n + 1):
        for w in range(int(maximum_cost) + 1):
            if i == 0 or w == 0:
                table[i][w] = 0.0
            elif actions[i-1]['cout'] <= w:
                table[i][w] = max(actions[i-1]['gain'] + table[i-1][int(w-actions[i-1]['cout'])], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    # Select
    w = maximum_cost
    selected_actions = []
    for i in range(n, 0, -1):
        if table[i][int(w)] != table[i-1][int(w)]:
            selected_actions.append(actions[i-1])
            w -= actions[i-1]['cout']

    return table[n][int(maximum_cost)], selected_actions



actions = transformData(listFromFile("/home/b/Documents/OCR/projet7/ph3/dataset1_Python+P7.csv"))
actions2 = transformData(listFromFile("/home/b/Documents/OCR/projet7/ph3/dataset2_Python+P7.csv"))



maximum_cost = 500

maximum_gain1, selection1 = sacADosFloat(actions, maximum_cost)
maximum_gain2, selection2 = sacADosFloat(actions2, maximum_cost)

print("\nDATASET 1")
print(f"Cout: {sum(x['cout'] for x in selection1):.2f}")
#print(f"Rendement: {sum((x['cout']*x['rendement']/100)for x in actions_selectionnees):.2f}")
print("Gain: %.2f" % maximum_gain1)
print(f"Actions sélectionnées: {[x['nom'] for x in selection1]}")

print("\nDATASET 2")
print(f"Cout: {sum(x['cout'] for x in selection2):.2f}")
#print(f"Rendement: {sum((x['cout']*x['rendement']/100)for x in actions_selectionnees2):.2f}")
print("Gain: %.2f" % maximum_gain2)
print(f"Actions sélectionnées: {[x['nom'] for x in selection2]}")
