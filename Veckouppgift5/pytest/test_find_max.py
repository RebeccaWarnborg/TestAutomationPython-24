# Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något

def find_max(lst):
    if not lst:  # Om listan är tom, returnera None
        return None
    return max(lst)  # Annars returnera största värdet

def test_positive_numbers():
    expected = 9
    actual = find_max([1, 5, 3, 9, 2])
    assert actual == expected

def test_negative_numbers():
    expected = -1
    actual = find_max([-10, -3, -50, -1])
    assert actual == expected

def test_mixed_numbers():
    expected = 7
    actual = find_max([-2, 0, 7, -5, 4])
    assert actual == expected

def test_single_element():
    expected = 42
    actual = find_max([42])
    assert actual == expected

def test_empty_list():
    expected = None
    actual = find_max([])
    assert actual == expected

def test_duplicate_values():
    expected = 3
    actual = find_max([3, 3, 3])
    assert actual == expected

