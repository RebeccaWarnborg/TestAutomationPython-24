# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. 
# Sedan ska man försöka gissa det. Om man gissar för lågt eller för högt ska spelet tala om det. 
# Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
import random
secret = random.randint(1, 100)

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")
while True:
    user_input = input ("Gissa:")
    try:
        guess = int(user_input)  # Omvandla inmatningen till ett heltal
        if guess < secret:
            print("För lågt! Försök igen.")
        elif guess > secret:
            print("För högt! Försök igen.")
        else: 
            print(f"Rätt! Talet jag tänkte på var {secret}. Bra jobbat!")
            break  # Avsluta loopen om användaren gissar rätt
    except ValueError:
        print("Ogiltig inmatning. Skriv in ett heltal.")