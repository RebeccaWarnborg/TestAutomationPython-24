# Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

for y in range(1, 7):  # 6 rader
    s = ""
    for x in range(1, 9):  # 8 kolumner
        if x == 1:  # Skriv "#" i första kolumnen
            s += "#"
        else:
            s += "."  # Resten av kolumnerna är "."
    print(s)

for y in range(1, 7):  # 6 rader
    s = ""
    for x in range(1, 9):  # 8 kolumner
        if x == y:  # Skriv "#" i kolumnen som motsvarar radens nummer
            s += "#"
        else:
            s += "."  # Resten av kolumnerna är "."
    print(s)