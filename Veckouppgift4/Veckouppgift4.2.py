# 1 Skriv en funktion som tar en sträng som parameter.
# När den anropas ska den skriva ut strängen och "är en fena på programmering". 
# Exempel: my_function("David") → "David är en riktig hacker"
from funktioner import my_function

my_function("David")  # Utskrift: David är en fena på programmering

my_function("Emma")  # Utskrift: Emma är en fena på programmering
my_function("Lisa")   # Utskrift: Lisa är en fena på programmering


# Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
# eko("hej") → skriver ut "hejhej"
# Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"

from funktioner import eko  # Direkt import från funktioner.py

eko("hej", 3)  # Förväntat utskrift: "hejhejhej"
eko("hallå", 5)  # Förväntat utskrift: "hallåhallåhallåhallå"
eko("123", 1)  # Förväntat utskrift: "123"
