# När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. 
# Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
# poker_hand(cards)
#"Du fick ett par med valören: 5"
# 1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. 
# Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]
# Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

import random

def draw_card():
    # Slumpar ett spelkort och returnerar det som en lista med [färg, valör].
    suits = ["ruter", "hjärter", "spader", "klöver"]
    value = random.randint(2, 14)
    suit = random.choice(suits)
    return [suit, value]

def same_value(card1, card2):
    # Jämför två spelkort och returnerar True om de har samma valör.
    return card1[1] == card2[1]

def poker_hand(cards):
    # Kollar om en pokerhand innehåller ett par och skriver ut resultatet.
    
    value_counts = {}  # Dictionary för att räkna valörer
    
    # Gå igenom alla kort i handen
    for card in cards:
        value = card[1]  # Hämta valören
        if value in value_counts:
            value_counts[value] += 1  # Öka räknaren om valören redan finns
        else:
            value_counts[value] = 1  # Lägg till ny valör
    
    # Kolla om någon valör förekommer exakt två gånger (ett par)
    for value, count in value_counts.items():
        if count == 2:
            print(f"Du fick ett par med valören: {value}")
            return  # Avsluta funktionen efter att vi hittat ett par

    print("Inget par hittades.")  # Om inget par finns

# Skapa en pokerhand med 5 slumpade kort
hand = [draw_card() for _ in range(5)]  

# Skriv ut handen
print("Din hand:", hand)

# Analysera handen
poker_hand(hand)