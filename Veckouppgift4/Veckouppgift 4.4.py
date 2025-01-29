# Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
# last([1, 2, 3]) → 3

def last(lista):
    return lista[-1]  # Returnerar sista elementet i listan

print(last([3, 2, 1]))  # Förväntat resultat: 3
print(last(["a", "y", "x"]))  # Förväntat resultat: "x"
print(last([10, 34, 67, 101]))  # Förväntat resultat: 101


# Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. 
# När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]

def cut_edges(lista):
    return lista[1:-1]  # Returnerar listan utan första och sista elementet
print(cut_edges([1, 2, 3, 4]))  # Förväntat resultat: [2, 3]
print(cut_edges([10, 20, 30, 40, 50]))  # Förväntat resultat: [20, 30, 40]