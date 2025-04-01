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

def sac_a_dos(actions, cout_maximal):
    n = len(actions)
    # Créer une table pour stocker les résultats des sous-problèmes
    table = [[0 for x in range(cout_maximal + 1)] for x in range(n + 1)]

    # Construire la table de programmation dynamique
    for i in range(n + 1):
        for w in range(int(cout_maximal) + 1):
            print(w - actions[i-1]['cout'])
            #print(w-actions[i-1])
            if i == 0 or w == 0:
                table[i][w] = 0.0
            elif actions[i-1]['cout'] <= w:
                table[i][w] = max(actions[i-1]['rendement'] + table[i-1][int(w-actions[i-1]['cout'])], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]


    for i in range(n + 1):
        print(f"\ntable[{i}][60]", table[i][60], i-1)
        print(f"actions[{i}-1]['rendement']", actions[i-1]['rendement'])
        print(f"table[{i}-1][(60-actions[{i}-1]['cout'])]", table[i-1][(60-actions[i-1]['cout'])])
        print(f"table[{i}-1][60]", table[i-1][60])
        print(f"actions[{i}-1]['rendement'] + table[{i}-1][(60-actions[{i}-1]['cout'])], table[{i}-1][60]", actions[i-1]['rendement'] + table[i-1][(w-actions[i-1]['cout'])], table[i-1][w])
    # Trouver les actions sélectionnées
    w = cout_maximal
    actions_selectionnees = []
    for i in range(n, 0, -1):
        if table[i][int(w)] != table[i-1][int(w)]:
            actions_selectionnees.append(actions[i-1])
            w -= actions[i-1]['cout']

    return table[n][cout_maximal], actions_selectionnees


def display_result():
    print(f"Rendement maximal: {rendement_maximal}%")
    print("Actions sélectionnees:")
    for action in actions_selectionnees:
        print(
            f"Nom: {action['nom']}, Cout: {action['cout']}, Rendement: {action['rendement']}%")

#actions = listFromFile("/home/b/Documents/OCR/projet7/actions.csv")
actions = listFromFile("/home/b/Documents/OCR/projet7/ph3/dataset1_Python+P7.csv")
# Conversion de la liste en dictionnaires pour faciliter l'accès
actions = [{'nom': action[0], 'cout': action[1], 'rendement': action[2]} for action in actions]

#print(actions[22]['cout'], type(actions[22]['cout']))
cout_maximal = 500
rendement_maximal, actions_selectionnees = sac_a_dos(actions, cout_maximal)

# display_result()
