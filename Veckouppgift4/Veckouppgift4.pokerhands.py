# När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. 
# Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
# poker_hand(cards)
#"Du fick ett par med valören: 5"
# 1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. 
# Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]

import random  # Steg 1: Importera modulen random

def draw_card():
    # Slumpar ett spelkort och returnerar det som en lista med [färg, valör].
    
    suits = ["ruter", "hjärter", "spader", "klöver"]  # Steg 2: Lista med färger
    value = random.randint(2, 14)  # Steg 3: Slumpa en valör mellan 2 och 14
    suit = random.choice(suits)  # Steg 4: Slumpa en färg
    
    return [suit, value]  # Steg 5: Returnera kortet som en lista

# Steg 6: Testa funktionen genom att skriva ut ett kort
print(draw_card())  