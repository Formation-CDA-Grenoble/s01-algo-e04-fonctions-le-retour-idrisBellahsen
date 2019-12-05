

def mix(list):
    from random import shuffle
    shuffle(list)
    
    return list
    # Fin de ton code



# Pas touche!
tests = (
    (["a", "b", "c"]),
    (["pomme", "banane", "orange"]),
    ([1, 2, 3]),
    (["a", "b", "c", 1, 2, 3]),
)

for test in tests:
    print(f"L'appel  mix({test})  renvoie: {mix(test)}")
