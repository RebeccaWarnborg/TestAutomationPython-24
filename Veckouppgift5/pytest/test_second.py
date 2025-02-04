# Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet

def find_2nd_max(numbers):
    if not numbers or len(numbers) < 2:
        return None 

    max_value = second_max = numbers[0]

    for item in numbers[1:]: 
        if item > max_value:
            second_max = max_value
            max_value = item
        elif item > second_max and item != max_value:
            second_max = item
    return second_max if second_max != max_value else None

def test_positive_numbers():
    expected = 5
    actual = find_2nd_max([1, 5, 3, 9, 2])
    assert actual == expected

def test_negative_numbers():
    expected = -3
    actual = find_2nd_max([-10, -3, -50, -1])
    assert actual == expected

def test_mixed_numbers():
    expected = 4
    actual = find_2nd_max([-2, 0, 7, -5, 4])
    assert actual == expected

def test_single_element():
    expected = None
    actual = find_2nd_max([42])
    assert actual == expected

def test_empty_list():
    expected = None
    actual = find_2nd_max([])
    assert actual == expected

def test_duplicate_values():
    expected = None
    actual = find_2nd_max([3, 3, 3])
    assert actual == expected