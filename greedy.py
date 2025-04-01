import csv

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

    def fractional_knapsack(capacity, items):
        # sort items by value-to-weight ration in descending order
        items.sort(key=lambda x: x.ratio, reverse=True)
        total_value = 0
        remaining_capacity = capacity
        for item in items:
            if remaining_capacity >= item.weight:
                total_value += item.value
                remaining_capacity -= item.weight
            else:
                total_value += item.ratio * remaining_capacity
                break
        return total_value



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


def greedy(capacity:int, items:[]):
    # sort items by value-to-weight ration in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    selected_items = []
    total_value = 0
    remaining_capacity = capacity
    for item in items:
        if remaining_capacity >= item.weight:
            total_value += item.value
            remaining_capacity -= item.weight
            selected_items.append(item)
        else:
            total_value += item.ratio * remaining_capacity
            break
    return selected_items, total_value