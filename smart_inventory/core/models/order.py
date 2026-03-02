from datetime import datetime
from core.models.order_item import OrderItem
from core.exceptions.invalid_quantity import InvalidQuantityException


class Order:
    def __init__(self, id: int, customer):
        self.id = id
        self.customer = customer
        self.order_date = datetime.now()
        self.items = []

    def add_item(self, product, quantity: int):
        if quantity <= 0:
            raise InvalidQuantityException("Quantity must be positive.")

        product.remove_stock(quantity)
        item = OrderItem(product, quantity)
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items)