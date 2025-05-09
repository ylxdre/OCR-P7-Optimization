import csv

MAX_COST = 500
FILE = "Liste+dactions+-+P7+Python+-+Feuille+1.csv"

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
        item[2] = item[1] * float(item[2].strip("%")) / 100
    return liste


def powerset(itemList):
    """
    Generate every subset (combination) for a given list
    :param itemList: a list of items
    :return: a list of combinations(lists)
    """
    result = [[]]
    for item in itemList:
        newsubsets = [subset + [item] for subset in result]
        result.extend(newsubsets)
    return result


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


def selectActions(actionList, maximal_cost):
    """
    select combination corresponding to max cost
    :param actionList: list of combinations
    :param maximal_cost: maximal cost
    :return: a list of selected items
    """
    best = []
    for i in actionList:
        cost = 0
        gain = 0
        for action in i:
            cost += action[1]
            gain += action[2]
        if cost < int(maximal_cost):
            best.append((gain, cost, i))

    sortedBest = sorted(best, key=lambda k: k[0], reverse=True)

    return sortedBest.pop(0)


def main():
    actions = listFromFile(FILE)
    power_actions = powerset(actions)
    selected_actions = selectActions(power_actions, MAX_COST)
    # tri des actions sur le rendement
    print("Cost:", selected_actions[1], "€")
    print("Profit: %.2f €" % selected_actions[0])
    print(f"Shares: {[x[0] for x in selected_actions[2]]}")


if __name__ == '__main__':
    main()
