def order(list):
    
    n = len(list)
    swap = True
    
    x = -1
    while swap:
        swap = False
        x = x + 1
        for i in range(1, n-x):
            if list[i - 1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                swap = True
  
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
