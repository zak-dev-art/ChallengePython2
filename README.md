# Coffee Shop Domain Modeling

## Overview
This project implements a domain model for a Coffee Shop using **Object-Oriented Programming (OOP) principles** in Python. The model consists of three main entities: `Customer`, `Coffee`, and `Order`. The system demonstrates object relationships, data validation, and aggregate methods, simulating real-world interactions within a coffee shop.

---

## Folder Structure
coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── debug.py
├── tests/
│ ├── test_customer.py
│ ├── test_coffee.py
│ └── test_order.py
├── Pipfile
└── README.md

markdown
Copy code

- `customer.py` - Contains the `Customer` class and related methods.
- `coffee.py` - Contains the `Coffee` class and related methods.
- `order.py` - Contains the `Order` class and related methods.
- `debug.py` - Optional file to test the classes interactively.
- `tests/` - Directory for unit tests using `pytest`.
- `Pipfile` - Manages project dependencies.

---

## Classes and Relationships

### 1. Customer
- Attributes:
  - `name`: String (1-15 characters)
- Methods:
  - `orders()`: Returns all orders placed by the customer.
  - `coffees()`: Returns a unique list of coffees ordered by the customer.
  - `create_order(coffee, price)`: Creates an order associated with the customer and coffee.
  - `most_aficionado(coffee)`: Class method to find the customer who spent the most on a specific coffee.

### 2. Coffee
- Attributes:
  - `name`: String (minimum 3 characters)
- Methods:
  - `orders()`: Returns all orders for this coffee.
  - `customers()`: Returns a unique list of customers who ordered this coffee.
  - `num_orders()`: Returns total number of orders.
  - `average_price()`: Returns the average price of this coffee based on orders.

### 3. Order
- Attributes:
  - `customer`: Customer instance
  - `coffee`: Coffee instance
  - `price`: Float (1.0 - 10.0)
- Relationships:
  - Each `Order` belongs to one `Customer` and one `Coffee`.

---

## Features
- Implements **many-to-many relationships** between `Customer` and `Coffee` through the `Order` class.
- Input validation for all attributes.
- Aggregate and helper methods for computing total orders, average price, and most-aficionado customer.
- Designed to be modular, clean, and testable.
