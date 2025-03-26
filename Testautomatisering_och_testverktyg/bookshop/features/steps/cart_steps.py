from behave import given, when, then
from shopping_cart import ShoppingCart

# Startläge: Tom varukorg
@given('en tom varukorg')
def step_impl(context):
    context.cart = ShoppingCart()

# Startläge: Varukorg med en bok
@given('en varukorg med boken "{title}"')
def step_impl(context, title):
    context.cart = ShoppingCart()
    context.cart.add_book(title, 259)  # priset som matchar feature-filen

# Startläge: Varukorg med flera böcker
@given('en varukorg med flera böcker')
def step_impl(context):
    context.cart = ShoppingCart()
    context.cart.add_book("Bok A", 150)
    context.cart.add_book("Bok B", 200)
    context.cart.add_book("Bok C", 170)

# När: Lägg till bok med pris
@when('jag lägger till boken "{title}" som kostar {price:d}kr')
def step_impl(context, title, price):
    context.cart.add_book(title, price)

# När: Lägg till samma bok två gånger
@when('jag lägger till boken "{title}" två gånger')
def step_impl(context, title):
    context.cart.add_book(title, 259)
    context.cart.add_book(title, 259)

# När: Ta bort bok
@when('jag tar bort boken "{title}"')
def step_impl(context, title):
    context.cart.remove_book(title)

# När: Töm varukorgen
@when('jag tömmer varukorgen')
def step_impl(context):
    context.cart.empty_cart()

# Då: Kontrollera antal böcker totalt
@then('ska varukorgen innehålla {count:d} bok')
def step_impl(context, count):
    assert context.cart.total_items() == count

# Då: Kontrollera antal exemplar av en bok
@then('ska varukorgen visa att boken har antal {quantity:d}')
def step_impl(context, quantity):
    assert list(context.cart.items.values())[0]["quantity"] == quantity

# Då: Kontrollera att varukorgen är tom
@then('ska varukorgen vara tom')
def step_impl(context):
    assert context.cart.is_empty()

# Då: Kontrollera totalsumman
@then('totalsumman ska vara {total:d}kr')
def step_impl(context, total):
    assert context.cart.total_price() == total