# Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.

end = 5
y = 1
for x in range(1, 100):
    y *= 2
    if x == end:  # Stoppa loopen efter 5 varv
        break
print(y)
