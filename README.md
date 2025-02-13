# DB_Test
Data Base automated testing 

# E-commerce Database Testing with pytest

This project demonstrates how to write automated tests for a PostgreSQL database using pytest and psycopg2.

## Prerequisites

*   Python 3.6+
*   PostgreSQL database
*   psycopg2-binary library (`pip install psycopg2-binary`)
*   pytest library (`pip install pytest`)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt  # If you have a requirements.txt file
    # Or:
    pip install pytest psycopg2-binary
    ```

4.  **Configure the database connection:**

    *   Edit the `conftest.py` file and update the following variables with your PostgreSQL database credentials:

        ```python
        DB_NAME = "test_ecommerce"
        DB_USER = "your_user"
        DB_PASSWORD = "your_password"
        DB_HOST = "localhost"
        DB_PORT = "5432"
        ```

    *   Make sure you have a PostgreSQL database named `test_ecommerce` and a user with the specified credentials.

5.  **Run the tests:**

    ```bash
    pytest -v
    ```

    This will run all the tests in the `test_db.py` file.

## Project Structure
my_ecommerce_project/
├── conftest.py # Pytest configuration and fixtures
├── test_db.py # The test file containing our tests
├── README.md # This file
└── requirements.txt # (Optional)

## Database Schema

The database schema consists of the following tables:

*   `products`: Stores information about products.
*   `customers`: Stores information about customers.
*   `orders`: Stores information about orders.
*   `order_items`: Stores the items in each order.

See the `conftest.py` file for the table definitions.

## Tests

The `test_db.py` file contains the following tests:

*   `test_product_price`: Verifies that the price of a product is correct.
*   `test_customer_order_count`: Verifies that the number of orders for a customer is correct.
*   `test_order_total`: Calculates the total value of an order and verifies that it matches the expected value.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## License

[Your License]
