class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)


class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iPhone", 699))

# Can we for-in the cart?
# what if it was to be sorted?
