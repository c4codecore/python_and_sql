import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def insert_student(name, age, grade):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    
    cursor.execute(insert_query, values)
    conn.commit()
    print(f"Student {name} added successfully!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_student("John Doe", 16, "10")
