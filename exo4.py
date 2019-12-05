def rankInsideStr(string, character):
    rank=0
    for letter in string:
        if letter == character:
            return rank
        rank+=1
    return None
    # Fin de ton code



# Pas touche!
tests = (
    ("pomme", "o", 1),
    ("pomme", "m", 2),
    ("pomme", "y", None),
    ("pomme", 3, None),
)

for test in tests:
    print(f"L'appel  rankInsideStr({test[0]}, {test[1]})  renvoie: {rankInsideStr(test[0], test[1])} (résultat attendu: {test[2]})")
