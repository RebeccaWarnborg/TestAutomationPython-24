# Gör ett program som upprepade gånger ber användaren skriva in ett tal. 
# När man skriver in ngen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen

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

# Här skrivs totalsumman ut när loopen avslutas
print(f"Det blir {summa} kr totalt. Välkommen åter!")