celcius = int(input("Skriv in en temperatur i grader Celsius:"))
fahrenheit = 1.8 * celcius + 32
print(f"Det blir {fahrenheit} grader  i fahrenheit")

temperatur = (input("Vill du ange temperaturen i celcius eller fahrenheit?: ")).lower() # frågar användaren vilken enhet av temperatur
if temperatur == "celcius":                  # om svaret blir celcius omvandlas det till fahrenheit
    celcius = float(input("Skriv temperatur i celcius: "))
    fahrenheit = (celcius * 1.8) + 32
    print(f"{celcius} grader celcius motsvarar {fahrenheit:.2f} grader fahrenheit")
elif temperatur == "fahrenheit":             # om svaret blir fahrenheit omvandlas det till celcius
    fahrenheit = float(input("Skriv temperaturen i fahrenheit: "))
    celcius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} grader fahrenheit motsvarar {celcius:.2f} grader celcius.")
else:                                        # om svaret är fel
    print("Fel, skriv celcius eller fahrenheit.")