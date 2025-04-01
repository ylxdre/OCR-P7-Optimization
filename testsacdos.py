import csv

def listFromFile(csv_file):
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

def sac_a_dos_float(actions, cout_maximal):
    n = len(actions)
    table = [[0.0 for x in range(int(cout_maximal) + 1)] for x in range(n + 1)]

    # Dynamic programing table
    for i in range(n + 1):
        for w in range(int(cout_maximal) + 1):
            if i == 0 or w == 0:
                table[i][w] = 0.0
            elif actions[i-1]['cout'] <= w:
                table[i][w] = max(actions[i-1]['rendement'] + table[i-1][int(w-actions[i-1]['cout'])], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    # Select
    w = cout_maximal
    actions_selectionnees = []
    for i in range(n, 0, -1):
        if table[i][int(w)] != table[i-1][int(w)]:
            actions_selectionnees.append(actions[i-1])
            w -= actions[i-1]['cout']

    return table[n][int(cout_maximal)], actions_selectionnees

actions = listFromFile("/home/b/Documents/OCR/projet7/ph3/dataset1_Python+P7.csv")
actionstmp = [{'nom': action[0], 'cout': action[1], 'rendement': action[2]} for action in actions if action[1] > 0.0]
actions = sorted(actionstmp, key=lambda x: x['cout'])

actions2 = listFromFile("/home/b/Documents/OCR/projet7/ph3/dataset2_Python+P7.csv")
actions2tmp = [{'nom': action[0], 'cout': action[1], 'rendement': action[2]} for action in actions2 if action[1] > 0.0]
actions2 = sorted(actions2tmp, key=lambda x: x['cout'])


cout_maximal = 500

valeur_maximale, actions_selectionnees = sac_a_dos_float(actions, cout_maximal)
valeur_maximale2, actions_selectionnees2 = sac_a_dos_float(actions2, cout_maximal)

print("\nDATASET 1\n")
print(f"Cout: {sum(x['cout'] for x in actions_selectionnees):.2f}")
print(f"Rendement: {sum((x['cout']*x['rendement']/100)for x in actions_selectionnees):.2f}")
print(f"Actions sélectionnées: {[x['nom'] for x in actions_selectionnees]}")

print("\nDATASET 2\n")
print(f"Cout: {sum(x['cout'] for x in actions_selectionnees2):.2f}")
print(f"Rendement: {sum((x['cout']*x['rendement']/100)for x in actions_selectionnees2):.2f}")
print(f"Actions sélectionnées: {[x['nom'] for x in actions_selectionnees2]}")
