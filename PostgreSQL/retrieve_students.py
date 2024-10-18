# retrieve_students.py

from db_connection import get_connection

def fetch_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()

    cur.close()
    conn.close()

    return students

if __name__ == "__main__":
    students = fetch_students()
    for student in students:
        print(student)
