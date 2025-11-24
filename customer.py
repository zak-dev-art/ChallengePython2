from typing import List
from order import Order
from coffee import Coffee

class Customer:
    all = []

    def __init__(self, name: str):
        self.name = name     # triggers setter
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value


    def orders(self) -> List["Order"]:
        return [o for o in Order.all if o.customer is self]

    def coffees(self) -> List["Coffee"]:
        return list({o.coffee for o in self.orders()})

    
    def create_order(self, coffee: Coffee, price: float):
        return Order(self, coffee, price)

    
    @classmethod
    def most_aficionado(cls, coffee: Coffee):
        
        # Find the customer who spent the most on a specific coffee
        customers_spending = {}

        for order in Order.all:
            if order.coffee is coffee:
                cust = order.customer
                customers_spending[cust] = customers_spending.get(cust, 0) + order.price

        if not customers_spending:
            return None

        # Return customer with highest spending
        return max(customers_spending, key=customers_spending.get)
