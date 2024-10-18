import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def create_table():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        grade VARCHAR(5)
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'students' created successfully")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()
