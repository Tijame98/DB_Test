import pytest
import psycopg2
from conftest import *

def test_product_price(db_connection):
    """Tests that the price of a product is correct."""
    cur = db_connection.cursor()
    product_name = "Laptop"
    expected_price = 1200.00

    cur.execute("SELECT price FROM products WHERE name = %s", (product_name,))
    result = cur.fetchone()

    assert result is not None
    assert result[0] == expected_price
    cur.close()

def test_customer_order_count(db_connection):
    """Tests that the number of orders for a customer is correct."""
    cur = db_connection.cursor()
    customer_email = "alice@example.com"
    expected_order_count = 1

    cur.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE customer_id = (SELECT id FROM customers WHERE email = %s)
    """, (customer_email,))
    result = cur.fetchone()

    assert result is not None
    assert result[0] == expected_order_count
    cur.close()

def test_order_total(db_connection):
    """Tests that the total value of an order is correct."""
    cur = db_connection.cursor()
    customer_email = "bob@example.com"
    expected_total = 150.00  # 2 Keyboards * 75.00

    cur.execute("""
        SELECT SUM(p.price * oi.quantity)
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        JOIN orders o ON oi.order_id = o.id
        JOIN customers c ON o.customer_id = c.id
        WHERE c.email = %s
    """, (customer_email,))
    result = cur.fetchone()

    assert result is not None
    assert result[0] == expected_total
    cur.close()