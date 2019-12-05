def order(list):
    
    list.sort()
    return list
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
    ([50, 0, -12, 0], [-12, 0, 0, 50]),
    (["pomme", "banane", "orange"], ["banane", "orange", "pomme"]),
)

for test in tests:
    print(f"L'appel  order({test[0]})  renvoie: {order(test[0])} (résultat attendu: {test[1]})")
