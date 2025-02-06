
from main_test_function import is_sorted_ascending

def test_is_sorted_ascending():
    # Fall där listan är sorterad
    numbers = [1, 2, 3, 4, 5]
    expected = True
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall där listan inte är sorterad
    numbers = [5, 3, 1, 2, 4]
    expected = False
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall med en tom lista (bör vara True)
    numbers = []
    expected = True
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall med en lista med ett element (bör vara True)
    numbers = [42]
    expected = True
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall där alla element är lika (bör vara True)
    numbers = [7, 7, 7, 7]
    expected = True
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall där listan innehåller negativa tal men är sorterad
    numbers = [-3, -2, -1, 0, 1]
    expected = True
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    # Fall där listan innehåller negativa tal och inte är sorterad
    numbers = [-1, -3, -2, 0, 1]
    expected = False
    actual = is_sorted_ascending(numbers)
    assert actual == expected, f"Fail: {numbers}, expected {expected}, got {actual}"

    print("Alla testfall passerade!")

# Kör testerna
test_is_sorted_ascending()