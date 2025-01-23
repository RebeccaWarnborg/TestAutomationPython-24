# Gör ett program som upprepade gånger ber användaren skriva in ett tal. 
# När man skriver in ngen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen
# Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
# Version 3: programmet ska fråga hur många procent dricks man vill lägga på. 
# Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

summa = 0

while True:
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    user_input = input ("Skriv in ett belopp:")

    if user_input.lower() == "quit":
        break # Avslutar loopen

    try:
        belopp = float(user_input) # Lägg till beloppet till summan här
        summa += belopp  # Här lägger du till beloppet till summan

    except ValueError:
        print("Det var inte ett giltigt tal, försök igen.")

# Fråga användaren hur många personer de är
antal_personer = int(input("Hur många är ni? ")) 

# Räkna ut hur mycket varje person ska betala
belopp_per_person = summa / antal_personer 

# Fråga hur många procent dricks användaren vill lägga
dricks_input = input("Hur många procent dricks vill ni lägga? (Lämna tomt för 10%): ")

# Om användaren lämnar fältet tomt, sätt dricks till 10%
if dricks_input.strip() == "":
    dricks_procent = 10
else:
    dricks_procent = int(dricks_input)

# Beräkna dricks och ny totalsumma
dricks = summa * (dricks_procent / 100)
ny_summa = summa + dricks

# Skriv ut totalsumman, dricks och belopp per person
print(f"Det blir {ny_summa:.2f} kr totalt, inklusive {dricks:.2f} kr i dricks.")
print(f"Alltså {ny_summa / antal_personer:.2f} kr per person. Välkommen åter!")