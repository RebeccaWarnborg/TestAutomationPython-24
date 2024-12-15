import math
# a = float (input ("Första sidan?"))
# b = float (input ("Andra sidan? "))
# c = math.sqrt (a**2 + b**2)
# print (f"Hyptenusans längd: {c:.2f}")


def cirkel_berakningar(radie):
    area = math.pi * radie**2
    omkrets = 2 * math.pi * radie 
    return area, omkrets 
radie = float(input("Ange cirkelns radie: "))
area , omkrets = cirkel_berakningar(radie)

print(f"För en cirkel med radie {radie}:")
print (f"Area: {area:.2f}")
print (f"Omkrets: {omkrets:.2f}")