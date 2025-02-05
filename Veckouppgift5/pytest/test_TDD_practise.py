# Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
#def c_to_f(degree):
 #   if degree < -273.15:
  #      return None
   # return degree * 9 / 5 + 32

import pytest
from Veckouppgift5.main_test_function import c_to_f

def test_c_to_f():
    test_cases = [
        (-273.15, -459.67),    # Gränsvärde, -273.15 C = -459.67 F
        (0, 32),               # 0 C = 32 F
        (100, 212),            # 100 C = 212 F
        (-40, -40),            # -40 C = -40 F (specialfall)
        (37, 98.6),            # Normal kroppstemperatur i C = 98.6 F
    ]

    for celsius, expected in test_cases:
        actual = c_to_f(celsius)
        assert actual == expected, f"Fel: c_to_f({celsius}) gav {actual}, förväntat {expected}"