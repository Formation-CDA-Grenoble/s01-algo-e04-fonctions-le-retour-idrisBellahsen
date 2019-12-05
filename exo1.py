def isInside(list, element):
    
  
    return element in list

    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, True),
    ([1, 2, 3], -1, False),
    (["pomme", "banane", "orange"], "pomme", True),
    (["pomme", "banane", "orange"], "cerise", False),
)

for test in tests:
    print(f"L'appel  isInside({test[0]}, {test[1]})  renvoie: {isInside(test[0], test[1])} (résultat attendu: {test[2]})")
