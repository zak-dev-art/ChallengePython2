import pytest
from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def setup_function():
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()

def test_order_initialization_and_validation():
    c = Customer("Alice")
    coffee = Coffee("Espresso")

    order = Order(c, coffee, 5.0)
    assert order.customer is c
    assert order.coffee is coffee
    assert order.price == 5.0

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)

    with pytest.raises(TypeError):
        Order(c, "not coffee", 5.0)

    with pytest.raises(TypeError):
        Order(c, coffee, "10")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 15.0)
