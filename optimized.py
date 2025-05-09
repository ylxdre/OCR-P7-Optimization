import csv

MAX_COST = 500
DATASET1 = "dataset1_Python+P7.csv"
DATASET2 = "dataset2_Python+P7.csv"
DATASET0 = "Liste+dactions+-+P7+Python+-+Feuille+1.csv"


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
        if item[2][-1] == "%":
            item[2] = item[2].strip("%")
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
               'ratio2': (x[1] * x[2] / 100) / x[1]}
              for x in dataset if x[1] > 0.0 and x[2] > 0.0]

    return sorted(tmpset, key=lambda x: x['gain'], reverse=True)


def get_results(filepath, maximum, nbr):
    """
    load, transform data then run the algorithm and print results
    :param filepath: full path to csv
    :param maximum: maximum cost
    :param nbr: set number
    :return: print results
    """

    action_list = transformData(listFromFile(filepath))
    maximum_gain, selection = sacADosFloat(action_list, maximum)

    print("\nDATASET", nbr)
    print(f"Cost: {sum(x['cout'] for x in selection):.2f} €")
    print("Profit: %.2f €" % maximum_gain)
    print(f"Shares : {[x['nom'] for x in selection]}")


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
                table[i][w] = (
                    max(
                        actions[i-1]['gain'] +
                        table[i-1][int(w-actions[i-1]['cout'])],
                        table[i-1][w]
                    )
                )

            else:
                table[i][w] = table[i-1][w]

    # Selection
    w = maximum_cost
    selected_actions = []
    for i in range(n, 0, -1):
        if table[i][int(w)] != table[i-1][int(w)]:
            selected_actions.append(actions[i-1])
            w -= actions[i-1]['cout']

    return table[n][int(maximum_cost)], selected_actions


def main():
    # get_results(DATASET0, MAX_COST, 0)
    get_results(DATASET1, MAX_COST, 1)
    get_results(DATASET2, MAX_COST, 2)


if __name__ == '__main__':
    main()
