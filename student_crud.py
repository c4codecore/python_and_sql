import psycopg2

# Function to Connect to PostgreSQL
def get_connection():
	try:
		return psycopg2.connect(
			database="mydb1",
			user="postgres",
			password="123",
			host="127.0.0.1",
			port=5432,
		)
	except:
		return False

conn = get_connection()

if conn:
	print("Connection to the PostgreSQL established successfully.")
else:
	print("Connection to the PostgreSQL encountered and error.")

cur = conn.cursor()

# Function to create the 'students' table
def create_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER,
        grade VARCHAR(10)
    );
    '''
    cur.execute(create_table_query)
    conn.commit()
    print("Table created successfully")

# Function to insert a new student (Create)
def insert_student(name, age, grade):
    insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id;"
    cur.execute(insert_query, (name, age, grade))
    student_id = cur.fetchone()[0]
    conn.commit()
    print(f"Student inserted with ID: {student_id}")

# Function to fetch all students (Read)
def fetch_students():
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    for student in students:
        print(student)

# Function to update a student's data (Update)
def update_student(student_id, name, age, grade):
    update_query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s;"
    cur.execute(update_query, (name, age, grade, student_id))
    conn.commit()
    print(f"Student with ID {student_id} updated.")

# Function to delete a student (Delete)
def delete_student(student_id):
    delete_query = "DELETE FROM students WHERE id = %s;"
    cur.execute(delete_query, (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} deleted.")

# Example usage
if __name__ == "__main__":
    # Step 1: Create the table
    create_table()

    # Step 2: Insert some students
    insert_student("Alice", 22, "A")
    insert_student("Bob", 20, "B")
    insert_student("Charlie", 23, "A")

    # Step 3: Fetch and display all students
    print("\nList of students:")
    fetch_students()

    # Step 4: Update a student's record
    update_student(2, "Bob Updated", 21, "B+")

    # Step 5: Fetch and display updated list of students
    print("\nList of students after update:")
    fetch_students()

    # Step 6: Delete a student
    delete_student(3)

    # Step 7: Fetch and display the final list of students
    print("\nList of students after deletion:")
    fetch_students()

    # Close the cursor and connection
    cur.close()
    conn.close()
