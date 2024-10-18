# create_table.py

from db_connection import get_connection

def create_students_table():
    conn = get_connection()
    cur = conn.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        grade VARCHAR(10)
    );
    '''
    try:
        cur.execute(create_table_query)
        conn.commit() # to save changes in DB 
        print("Students table created successfully.")
    except Exception as ex:
        print("Could not execute query", ex)
    finally:
        cur.close()
        conn.close()
    
create_students_table()
