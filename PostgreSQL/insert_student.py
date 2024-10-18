# insert_student.py

from db_connection import get_connection

def insert_student(name, age, grade):
    conn = get_connection()
    cur = conn.cursor()

    insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id;"
    cur.execute(insert_query, (name, age, grade))
    
    student_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    print(f"Student inserted with ID: {student_id}")

insert_student("Amitabh Bachan", 85, 76.8)