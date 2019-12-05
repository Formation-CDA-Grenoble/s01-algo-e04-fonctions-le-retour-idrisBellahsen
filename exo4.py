def rankInsideStr(string, character):
    rank=string.find(str(character))
    if rank == -1:
        return None 
    return rank
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
