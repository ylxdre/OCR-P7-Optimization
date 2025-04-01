def permute(liste):
    if len(liste) == 0:
        return []

    if len(liste) == 1:
        return [liste]

    permutations = []

    for i in range(len(liste)):
        current = liste[i]
        remaining = liste[:i] + liste[i+1:]

        for p in permute(remaining):
            permutations.append([current] + p)

    return permutations



liste = []

for i in range(1, 6):
    liste.append(i)


test = permute(liste)
print(test)
