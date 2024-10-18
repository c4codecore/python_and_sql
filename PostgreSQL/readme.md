# Student Management System with PostgreSQL

This project provides a simple Python-based CRUD (Create, Read, Update, Delete) operation system for managing students in a PostgreSQL database. Each task (e.g., creating tables, inserting, updating, fetching, and deleting records) is organized into separate Python scripts for better maintainability.

## Prerequisites

- Python 3.x (preferably 3.12.4 or compatible)
- PostgreSQL installed and running
- `psycopg2-binary` and `python-dotenv` Python packages (install via `pip`)
  
To install the required packages, use:
```bash
pip install psycopg2-binary python-dotenv
```

## Setup

1. Clone or download the repository.

Steps to clone a Git repository:

1. **Install Git**  
   First, ensure Git is installed on your machine. You can download it from [Git's official site](https://git-scm.com/). 

2. **Navigate to the desired directory**  
   Open your terminal (or command prompt) and navigate to the directory where you want to clone the repository:
   ```bash
   cd /path/to/your/directory
   ```

3. **Clone the repository**  
   Use the following command to clone the repository:
   ```bash
   git clone <repository_url>
   ```
   For example:
   ```bash
   git clone https://github.com/c4codecore/python_and_sql.git
   ```

4. **Navigate into the cloned repository**  
   After cloning, move into the repository folder:
   ```bash
   cd python_and_sql
   ```

5. **Optional: Set up your Git identity**  
   If you haven’t configured Git with your username and email, you can do it now:
   ```bash
   git config user.name "<your_name>"
   git config user.email "<your_email>"
   ```


2. Ensure that you have PostgreSQL installed and running.
3. Create a `.env` file in your project directory with the following content:

   ```bash
   DB_NAME=your_db_name
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Update the `.env` file with your actual PostgreSQL credentials.

5. You're ready to run the scripts!

## Usage

Each task is handled by a separate script. Run the following scripts to perform CRUD operations:

### 1. Create Table

Run `create_table.py` to create the `students` table in your PostgreSQL database.

```bash
python create_table.py
```

### 2. Insert Data

Run `insert_student.py` to insert a new student into the `students` table.

```bash
python insert_student.py
```

You can customize the student details by modifying the function call in the script:
```python
insert_student("John Doe", 15, "10th")
```

### 3. Fetch Data

Run `retrieve_students.py` to fetch and display all student records.

```bash
python retrieve_students.py
```

### 4. Update Data

Run `update_student.py` to update an existing student's information. By default, it updates the student with ID 1.

```bash
python update_student.py
```

You can modify the script to update specific student details:
```python
update_student(1, age=16, grade="11th")
```

### 5. Delete Data

Run `delete_student.py` to delete a student by their ID.

```bash
python delete_student.py
```

You can change the student ID in the script to delete a specific student:
```python
delete_student(1)
```

## Folder Structure

```
.
├── db_connection.py    # Database connection script using .env
├── .env                # Environment variables for credentials
├── create_table.py     # Script to create the students table
├── insert_student.py   # Script to insert a student
├── retrieve_students.py# Script to fetch student data
├── update_student.py   # Script to update student data
└── delete_student.py   # Script to delete a student
```

## License

This project is open-source and free to use.

---