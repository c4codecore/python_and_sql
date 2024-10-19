# db_connection.py
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_connection():
    try:
        
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
    except:
        print("connection did not created",ex)
con = get_connection()
if con:
    print("connection establish sucessfully.")
else:
    print("connection did not establish.")       
