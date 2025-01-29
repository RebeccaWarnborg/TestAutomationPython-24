# 1 Skriv en funktion som tar en sträng som parameter.
# När den anropas ska den skriva ut strängen och "är en fena på programmering". 
# Exempel: my_function("David") → "David är en riktig hacker"

from funktioner import my_function

my_function("David")  # Utskrift: David är en fena på programmering

my_function("Emma")  # Utskrift: Emma är en fena på programmering
my_function("Lisa")   # Utskrift: Lisa är en fena på programmering


from funktioner import eko  # Direkt import från funktioner.py

eko("hej")  # Anropa funktionen direkt utan att använda modulnamn
