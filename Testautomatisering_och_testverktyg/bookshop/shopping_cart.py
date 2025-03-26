class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_book(self, title, price):
        if title in self.items:
            self.items[title]["quantity"] += 1
        else:
            self.items[title] = {"price": price, "quantity": 1}

    def remove_book(self, title):
        if title in self.items:
            del self.items[title]

    def empty_cart(self):
        self.items = {}

    def total_items(self):
        return sum(item["quantity"] for item in self.items.values())

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    def get_quantity(self, title):
        return self.items.get(title, {}).get("quantity", 0)

    def is_empty(self):
        return not self.items