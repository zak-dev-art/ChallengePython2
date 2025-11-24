import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def setup_function():
    # Reset all class-level lists before each test
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()


def test_customer_name_validation():
    # valid
    c = Customer("Alice")
    assert c.name == "Alice"

    # invalid: not string
    with pytest.raises(TypeError):
        Customer(123)

    # invalid: too long
    with pytest.raises(ValueError):
        Customer("ABCDEFGHIJKLMNOP")  # 16 characters


def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")

    c.create_order(coffee1, 3.0)
    c.create_order(coffee2, 4.0)
    c.create_order(coffee1, 2.5)

    # orders
    assert len(c.orders()) == 3

    # coffees
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

    c1.create_order(coffee, 5.0)  # total 5
    c2.create_order(coffee, 3.0)  # total 3
    c2.create_order(coffee, 4.0)  # total 7

    assert Customer.most_aficionado(coffee) is c2

    # no orders yet
    coffee2 = Coffee("Latte")
    assert Customer.most_aficionado(coffee2) is None
