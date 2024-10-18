import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def update_student(student_id, new_name, new_age, new_grade):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    update_query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    values = (new_name, new_age, new_grade, student_id)
    
    cursor.execute(update_query, values)
    conn.commit()
    print(f"Student with ID {student_id} updated successfully!")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    update_student(1, "Jane Doe", 17, "11")
