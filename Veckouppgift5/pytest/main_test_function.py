# Funktion för att omvandla grader Celsius till grader Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32
    
def count_words(sentence):
    if sentence:  # isalpha() kollar om hela strängen bara innehåller bokstäver
        return len(sentence.split())  # Dela upp strängen i ord och räkna dem
    else:
        return None  # Returnera None om strängen inte bara innehåller bokstäver
    
def is_sorted_ascending(numbers):
    return numbers == sorted(numbers)

