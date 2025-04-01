from importactions import listFromFile, listFromFile2

def sac_a_dos(actions, cout_maximal):
    n = len(actions)
    # Créer une table pour stocker les résultats des sous-problèmes
    table = [[0 for x in range(cout_maximal + 1)] for x in range(n + 1)]

    # Construire la table de programmation dynamique
    for i in range(n + 1):
        for w in range(cout_maximal + 1):
            #print('\ni', i, 'w', w)
            #print(actions[i-1]['cout'], )
            if i == 0 or w == 0:
                table[i][w] = 0
            elif actions[i-1]['cout'] <= w:
                table[i][w] = max(actions[i-1]['rendement'] + table[i-1][(w-actions[i-1]['cout'])], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    # Trouver les actions sélectionnées
    w = cout_maximal
    actions_selectionnees = []
    for i in range(n, 0, -1):
        if table[i][w] != table[i-1][w]:
            actions_selectionnees.append(actions[i-1])
            w -= actions[i-1]['cout']

    return table[n][cout_maximal], actions_selectionnees


def display_result():
    print(f"Rendement : {sum(x['cout'] * x['rendement']/100 for x in actions_selectionnees)}€")
    print(f"Cout: {sum(x['cout'] for x in actions_selectionnees)}€")
    print("Actions sélectionnees:")
    for action in actions_selectionnees:
        print(
            f"Nom: {action['nom']}, Cout: {action['cout']}, Rendement: {action['rendement']}%")

actions = listFromFile("/home/b/Documents/OCR/projet7/actions.csv")
#actions = listFromFile2("/home/b/Documents/OCR/projet7/ph3/dataset1_Python+P7.csv")
# Conversion de la liste en dictionnaires pour faciliter l'accès
actions = [{'nom': action[0], 'cout': action[1], 'rendement': action[2]} for action in actions]

#print(actions[22]['cout'], type(actions[22]['cout']))
cout_maximal = 500
rendement_maximal, actions_selectionnees = sac_a_dos(actions, cout_maximal)

display_result()
