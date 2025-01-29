# Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. 
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har. 
# Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

def pretty_print(lista):
    if len(lista) == 0:  # Kollar om listan är tom
        print("Listan är tom.")
    else:
        print(f"Listan har {len(lista)} element:")  # Skriver ut antalet element
        for index, element in enumerate(lista, start=1):  # Går igenom listan med index
            print(f"{index}. {element}")  # Skriver ut varje element

pretty_print(["a", "b", 3.14])
pretty_print([])  # Förväntat resultat: "Listan är tom."