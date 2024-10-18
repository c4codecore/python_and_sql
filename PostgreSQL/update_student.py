# update_student.py

from db_connection import get_connection

def update_student(student_id, name=None, age=None, grade=None):
    conn = get_connection()
    cur = conn.cursor()

    update_query = "UPDATE students SET"
    updates = []
    params = []

    if name:
        updates.append("name = %s")
        params.append(name)
    if age:
        updates.append("age = %s")
        params.append(age)
    if grade:
        updates.append("grade = %s")
        params.append(grade)

    update_query += ", ".join(updates) + " WHERE id = %s"
    params.append(student_id)

    cur.execute(update_query, params)
    conn.commit()

    cur.close()
    conn.close()

    print(f"Student with ID {student_id} updated.")

if __name__ == "__main__":
    update_student(1, age=16, grade="11th")
