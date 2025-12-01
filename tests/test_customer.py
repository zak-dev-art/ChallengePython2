import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def setup_function():
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()

def test_customer_name_validation():
    c = Customer("Alice")
    assert c.name == "Alice"

    with pytest.raises(TypeError):
        Customer(123)

    with pytest.raises(ValueError):
        Customer("ABCDEFGHIJKLMNOP")  # 16 chars

def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")

    c.create_order(coffee1, 3.0)
    c.create_order(coffee2, 4.0)
    c.create_order(coffee1, 2.5)

    assert len(c.orders()) == 3
    assert set(c.coffees()) == {coffee1, coffee2}

def test_create_order_creates_order_instance():
    c = Customer("James")
    coffee = Coffee("Espresso")

    order = c.create_order(coffee, 5.0)

    assert order.customer is c
    assert order.coffee is coffee
    assert order.price == 5.0

def test_most_aficionado():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Cappuccino")

    c1.create_order(coffee, 5.0)
    c2.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)

    assert Customer.most_aficionado(coffee) is c2

    coffee2 = Coffee("Latte")
    assert Customer.most_aficionado(coffee2) is None
