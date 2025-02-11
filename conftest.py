import pytest
import psycopg2

# Database connection settings (adjust to your environment)
DB_NAME = "test_db"  # Consider a dedicated testing database
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

@pytest.fixture(scope="session")
def db_connection():
    """Creates a database connection and yields it."""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        yield conn  # Provide the connection to the tests
    finally:
        if conn:
            conn.close()

@pytest.fixture(scope="session", autouse=True)
def setup_db(db_connection):
    """Sets up the database schema and cleans it up after the tests."""
    cur = db_connection.cursor()
    try:
        # Create the users table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            )
        """)
        db_connection.commit()
        yield  # Let the tests run
    finally:
        # Clean up:  Drop the table after all tests are finished
        cur.execute("DROP TABLE IF EXISTS users")
        db_connection.commit()
        cur.close()
