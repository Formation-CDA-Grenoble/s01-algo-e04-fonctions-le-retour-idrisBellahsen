def concatenate(list):
    result=""
    for item in list:
        result=result+str(item)
    return result    
    # Fin de ton code



# Pas touche!
tests = (
    (["a", "b", "c"], "abc"),
    (["pomme", "banane", "orange"], "pommebananeorange"),
    ([1, 2, 3], "123"),
    (["a", "b", "c", 1, 2, 3], "abc123"),
)

for test in tests:
    print(f"L'appel  concatenate({test[0]})  renvoie: {concatenate(test[0])} (résultat attendu: {test[1]})")
