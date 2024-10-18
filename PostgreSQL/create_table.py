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
    cur.execute(create_table_query)
    conn.commit()

    cur.close()
    conn.close()
    
    print("Students table created successfully.")

if __name__ == "__main__":
    create_students_table()
