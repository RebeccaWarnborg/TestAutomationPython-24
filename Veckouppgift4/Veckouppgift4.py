print("1a")
def foo(t):
    print("test")

foo("hej")

print("1b")
def fun1(x, y):
    return x * y

print(3, 5)

print("1c")
def fun1(x, y):
    return x * y

print(fun1(3, 5))

print("1d")
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
5(52+53)
print(a)

print("1e")
a = 5
def fun3(a):
    a += 1

a += 2
#a = a + 2
print(a)
⁠

print("1f")
def foo(i):
    return 2ii

def goo(x, y):
    return x(y)

a = goo(foo, 3)
print(a)
⁠

print("1g")

# Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

print("1h")
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

lista = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(lista)

print("1i")

# En uppgift i tre delar:Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.
def find_min(numbers):
    counter = None
    for item in numbers:
        if counter is None:
            counter = item
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])