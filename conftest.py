import pytest
import psycopg2

# Database connection settings (adjust to your environment)
DB_NAME = "test_db"  # Consider a dedicated testing database
DB_USER = "houssine"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"  # Default PostgreSQL port

with open('schema.sql', 'r') as f:
	schema = f.read()

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
        print("Connectd to database")
    finally:
        if conn:
            conn.close()

@pytest.fixture(scope="session", autouse=True)
def setup_db(db_connection):
    """Sets up the database schema and cleans it up after the tests."""
    cur = db_connection.cursor()
    try:
        # Create the users table if it doesn't exist
        cur.execute(schema)
        db_connection.commit()
        yield  # Let the tests run
        print("Tables are created")
    finally:
        # Clean up:  Drop the table after all tests are finished
        db_connection.commit()
        cur.close()
