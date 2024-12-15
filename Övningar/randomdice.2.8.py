# Ett program som simulerar ett tärningskast.
import random            # Importerar funktionen random som slumpvis tar fram ett tal.
print('Tärningarna är kastade!')
tärning1 = random.randint(1,6)     # Slumtal mellan 1 och 6.
tärning2 = random.randint(1,6)     # Slumtal mellan 1 och 6.
summan = tärning1 + tärning2       # Summan av de två kasten.
print(f'Du fick {tärning1} och {tärning2}, summan är {summan}')     # Utskriften av de två kasten.          