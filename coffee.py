from typing import List
from order import Order

class Coffee:
    all = []

    def __init__(self, name: str):
        self.name = name
        Coffee.all.append(self)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    
    def orders(self) -> List["Order"]:
        return [o for o in Order.all if o.coffee is self]

    def customers(self) -> List["Customer"]:
        return list({o.customer for o in self.orders()})

    
    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        prices = [o.price for o in self.orders()]
        return sum(prices) / len(prices) if prices else 0.0
