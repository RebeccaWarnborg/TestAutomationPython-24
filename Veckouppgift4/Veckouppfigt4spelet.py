# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. 
# Förr eller senare kommer man förbi 21. 
# Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

# I stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa tal. 
# Exempel: card = random.randint(1, 13)

import random  # Importera random-modulen

def first_over_21():
    total_summa = 0  # Starta med summan 0

    # Lägg till slumpade tal mellan 1 och 13 tills summan blir större än 21
    while total_summa <= 21:
        card = random.randint(1, 13)  # Slumpa ett tal mellan 1 och 13
        total_summa += card  # Lägg till det slumpade talet i summan
        
        # Kontrollera om summan nu är större än 21
        if total_summa > 21:
            print(f"Det första kortet som gör att summan blir större än 21 är {card}.")
            break  # Avsluta loopen när summan blir större än 21

# Anropa funktionen för att köra den
first_over_21()
