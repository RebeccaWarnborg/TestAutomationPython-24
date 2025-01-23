# Gör ett program som upprepade gånger ber användaren skriva in ett tal. 
# När man skriver in ngen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen
# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.

summa = 0

while True:
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    user_input = input ("Skriv in ett belopp:")

    if user_input.lower() == "quit":
        break  # Avslutar loopen

    try:
        belopp = float(user_input) # Lägg till beloppet till summan här
        summa += belopp  # Här lägger du till beloppet till summan

    except ValueError:
        print("Det var inte ett giltigt tal, försök igen.")

# Fråga användaren hur många personer de är
antal_personer = int(input("Hur många är ni? "))

# Räkna ut hur mycket varje person ska betala
belopp_per_person = summa / antal_personer

# Skriv ut totalsumman och vad varje person ska betala
print(f"Det blir {summa} kr totalt, alltså {belopp_per_person:.2f} kr per person. Välkommen åter!")