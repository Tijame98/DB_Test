import psycopg2 as pg
import pytest

@pytest.fixture(scope="session")
def db_connection():
    with open('schema.sql', 'r') as f:
	    schema = f.read()
 
    conn = pg.connect(dbname = 'test_db', user = 'houssine', password = 'admin', host = 'localhost', port = '5432')
    if(conn):
        print("Connectd to database")	
    else:
        print("Connexion Failed")

    yield conn
    
    cur = conn.cursor()
    cur.execute(schema)
    conn.commit()
    print('Tables are created')
    cur.close()
    conn.close()

@pytest.fixture(scope="session", autouse=True)
def setup_db(db_connection):
    with open('insert.sql', 'r') as f:
	    schema = f.read()
		
    cur = db_connection.cursor()
    cur.execute(schema)
    db_connection.commit()

    yield

    print("Insertion successful")

    db_connection.commit()
    cur.close()
    

    print('Data base is set up')