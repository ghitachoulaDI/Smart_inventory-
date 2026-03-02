from core.exceptions.invalid_quantity import InvalidQuantityException
from core.exceptions.out_of_stock import OutOfStockException


class Product:
    def __init__(self, id: int, name: str, category: str, price: float, quantity_in_stock: int):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def add_stock(self, qty: int) -> None:
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive.")
        self.quantity_in_stock += qty

    def remove_stock(self, qty: int) -> None:
        if qty <= 0:
            raise InvalidQuantityException("Quantity must be positive.")
        if qty > self.quantity_in_stock:
            raise OutOfStockException("Not enough stock available.")
        self.quantity_in_stock -= qty

    def get_value_in_stock(self) -> float:
        return self.price * self.quantity_in_stock