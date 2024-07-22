from typing import Iterator


class CartItem:
    def __init__(self, name: str, price: float):
        self.price = price
        self.name = name


class ShoppingCart:
    def __init__(self):
        self.items: list[CartItem] = []

    def add_item(self, it: CartItem):
        self.items.append(it)

    def __iter__(self) -> Iterator[CartItem]:
        return iter(self.items)


cart = ShoppingCart()
cart.add_item(CartItem("guitar", 799))
cart.add_item(CartItem("cd", 19))
cart.add_item(CartItem("iPhone", 1699))

# Can we for-in the cart?
# what if it was to be sorted?

print("Items in your cart.")
for item in cart:
    print(f" * {item.name} ${item.price:,}")
