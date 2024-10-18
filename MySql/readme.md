# MySQL CRUD Operations with Python

This project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations on a MySQL database using Python. The operations are separated into different Python scripts, and database credentials are managed through environment variables using a `.env` file.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.7+ installed on your system
- MySQL server installed and running
- The following Python packages installed:
  - `mysql-connector-python`
  - `python-dotenv`

To install the required packages, run:

```bash
pip install mysql-connector-python python-dotenv
```

### Setting up MySQL

1. **Create a MySQL database** named `school` (or any name you prefer).
   ```sql
   CREATE DATABASE school;
   ```

2. **Create a `.env` file** in the project directory and add your MySQL credentials:

   ```
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=school
   ```

## Project Structure

The project contains the following files:

```bash
.
├── create_table.py        # Script to create the students table
├── insert_student.py      # Script to insert a student record
├── retrieve_students.py   # Script to retrieve all student records
├── update_student.py      # Script to update a student record
├── delete_student.py      # Script to delete a student record
├── .env                   # Environment variables for MySQL credentials
└── README.md              # Project documentation (this file)
```

## Steps to Run Each File

1. **Create Table:**  
   Run `create_table.py` to create the `students` table.

   ```bash
   python create_table.py
   ```

2. **Insert Data:**  
   Run `insert_student.py` to insert a new student record into the `students` table.

   ```bash
   python insert_student.py
   ```

   You can modify the `name`, `age`, and `grade` values inside the script before running.

3. **Fetch Data:**  
   Run `retrieve_students.py` to fetch and display all student records from the `students` table.

   ```bash
   python retrieve_students.py
   ```

4. **Update Data:**  
   Run `update_student.py` to update an existing student's information by their ID.

   ```bash
   python update_student.py
   ```

   You can modify the `student_id`, `new_name`, `new_age`, and `new_grade` values inside the script before running.

5. **Delete Data:**  
   Run `delete_student.py` to delete a student record by their ID.

   ```bash
   python delete_student.py
   ```

   You can modify the `student_id` value inside the script before running.

## Example CRUD Operations

Here’s a summary of the CRUD operations performed by the scripts:

- **Create:** Creates a `students` table if it doesn't exist.
- **Insert:** Adds a new student to the table.
- **Read:** Retrieves all students from the table.
- **Update:** Updates a student’s information by ID.
- **Delete:** Removes a student record from the table by ID.

## Environment Variables

The `.env` file should contain your MySQL credentials:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school
```