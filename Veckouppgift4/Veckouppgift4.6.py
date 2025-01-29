# 7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y. 
# Båda ska vara tal. Funktionen ska returnera medelvärdet. 
# Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.

def average(x, y):
    return (x + y) / 2  # Beräknar medelvärdet

print(average(12, 18))  # Förväntat resultat: 15.0
print(average(25, 75))  # Förväntat resultat: 50.0
print(average(-10, 30))  # Förväntat resultat: 10.0
print(average(7.2, 14.8))  # Förväntat resultat: 11.0
print(average(100, 200))  # Förväntat resultat: 150.0
