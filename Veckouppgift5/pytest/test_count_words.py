# Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. 
# Ett ord är en serie tecken som separeras av mellanslag. 
# Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

# Task: Testa kod som ska returnera antalet ord från en sträng.
# Acceptanskritierier:
# Koden ska kunna returnera stora och små bokstäver.
# Om annat än bokstäver skrivs så ska resultatet bli None.
# Koden ska ignorera tecken och siffror i en sträng med text.
# Resultatet ska bli None om ordet är blandat med siffor. 

from main_test_function import count_words


def test_count_words():
    test_cases = [
        ("HELLO WORLD"),
        ("hello world"),
        ("Hello World!"),
        ("H3ll0 w0rld") ,
    ]
    #for count_words in test_cases:
     #   actual = count_words(test_cases)
      #  assert actual == expected
    for words in test_cases:
        expected = 2
        actual = count_words(words)
        assert actual == expected