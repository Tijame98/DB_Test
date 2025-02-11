import pytest

def test_insert_user(db_connection):
    """Tests that a user can be inserted into the database."""
    cur = db_connection.cursor()
    name = "Alice Smith"
    email = "alice@example.com"

    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db_connection.commit()

    cur.execute("SELECT id, name, email FROM users WHERE email = %s", (email,))
    result = cur.fetchone()

    assert result is not None
    assert result[1] == name
    assert result[2] == email
    cur.close()

def test_get_user_by_email(db_connection):
    """Tests that a user can be retrieved from the database by email."""
    cur = db_connection.cursor()
    # First, insert a user (assuming test_insert_user passed)
    name = "Bob Johnson"
    email = "bob@example.com"

    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db_connection.commit()

    # Retrieve the user by email
    cur.execute("SELECT id, name, email FROM users WHERE email = %s", (email,))
    result = cur.fetchone()

    assert result is not None
    assert result[1] == name
    assert result[2] == email
    cur.close()

def test_unique_email_constraint(db_connection):
    """Tests that the unique email constraint is enforced."""
    cur = db_connection.cursor()
    name1 = "Charlie Brown"
    email = "charlie@example.com"
    name2 = "Charles Browning" # Different name, same email

    # Insert the first user
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name1, email))
    db_connection.commit()

    # Attempt to insert a second user with the same email
    with pytest.raises(psycopg2.errors.UniqueViolation):
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name2, email))
        db_connection.commit()
    db_connection.rollback() # Important: Rollback to avoid issues with subsequent tests
    cur.close()
