# Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)

def count_vowels(word):
    vowels = "aeiouyåäöAEIOUYÅÄÖ"  # Inkluderar stora och små bokstäver
    return sum(1 for char in word if char in vowels)

def test_count_vowels():
    assert count_vowels("qwrt") == 0  # Inga vokaler
    assert count_vowels("Tt") == 0  # Inga vokaler
    assert count_vowels("123 123") == 0  # Endast siffror och mellanslag
    assert count_vowels("") == 0  # Tom sträng
    assert count_vowels("hello") == 2  # "e" och "o"
    assert count_vowels("HELLO") == 2  # Stora bokstäver
    assert count_vowels("aåäöy") == 5  # Alla svenska vokaler
    assert count_vowels("Python!") == 2  # Blandade tecken

