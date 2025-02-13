-- Products
INSERT INTO products (name, description, price) VALUES
('Laptop', 'High-performance laptop', 1200.00),
('Mouse', 'Wireless mouse', 25.00),
('Keyboard', 'Mechanical keyboard', 75.00);

-- Customers
INSERT INTO customers (name, email, address) VALUES
('Alice Smith', 'alice@example.com', '123 Main St'),
('Bob Johnson', 'bob@example.com', '456 Oak Ave');

-- Orders
INSERT INTO orders (customer_id, order_date) VALUES
((SELECT id FROM customers WHERE email = 'alice@example.com'), '2023-10-26'),
((SELECT id FROM customers WHERE email = 'bob@example.com'), '2023-10-27');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity) VALUES
((SELECT id FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'alice@example.com')), (SELECT id FROM products WHERE name = 'Laptop'), 1),
((SELECT id FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'alice@example.com')), (SELECT id FROM products WHERE name = 'Mouse'), 1),
((SELECT id FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'bob@example.com')), (SELECT id FROM products WHERE name = 'Keyboard'), 2);