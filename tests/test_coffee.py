import pytest
from coffee import Coffee
from customer import Customer
from order import Order


def setup_function():
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()


def test_coffee_name_validation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

    # invalid: not string
    with pytest.raises(TypeError):
        Coffee(123)

    # invalid: too short
    with pytest.raises(ValueError):
        Coffee("Hi")


def test_coffee_relationships():
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    coffee = Coffee("Mocha")

    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)
    c1.create_order(coffee, 5.0)

    assert len(coffee.orders()) == 3
    assert set(coffee.customers()) == {c1, c2}


def test_num_orders_and_average_price():
    c = Customer("Alice")
    coffee = Coffee("Latte")

    c.create_order(coffee, 3.0)
    c.create_order(coffee, 5.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == (3.0 + 5.0) / 2

    # no orders
    coffee2 = Coffee("Mocha")
    assert coffee2.num_orders() == 0
    assert coffee2.average_price() == 0.0
