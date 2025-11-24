import pytest
from order import Order
from customer import Customer
from coffee import Coffee


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

    # invalid customer
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)

    # invalid coffee
    with pytest.raises(TypeError):
        Order(c, "not coffee", 5.0)

    # invalid price type
    with pytest.raises(TypeError):
        Order(c, coffee, "10")

    # invalid price range
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 15.0)
