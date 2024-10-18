import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def delete_student(student_id):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    delete_query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    
    cursor.execute(delete_query, values)
    conn.commit()
    print(f"Student with ID {student_id} deleted successfully!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    delete_student(1)