# delete_student.py

from db_connection import get_connection

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    delete_query = "DELETE FROM students WHERE id = %s;"
    cur.execute(delete_query, (student_id,))
    
    conn.commit()

    cur.close()
    conn.close()

    print(f"Student with ID {student_id} deleted.")

if __name__ == "__main__":
    delete_student(1)
