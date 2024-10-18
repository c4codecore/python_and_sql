# db_connection.py
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_connection():
    try:
        # Create and return a new database connection
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connection established successfully!")
        return connection
    except Exception as ex:
        print("Connection could not be created:", ex)

if __name__ == "__main__":
    con = get_connection()
