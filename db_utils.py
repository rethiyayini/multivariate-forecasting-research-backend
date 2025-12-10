# db_utils.py
import psycopg2  # Or your preferred database library
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")

def get_db_connection():
    """Establishes and returns a database connection."""
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")  # Handle or log the error
        return None  # Or raise the exception if you prefer

def close_db_connection(conn):
    """Closes a database connection."""
    if conn:
        try:
            conn.close()
        except psycopg2.Error as e:
            print(f"Error closing connection: {e}")

# Example usage (within the db_utils.py file for testing):
if __name__ == '__main__':
    conn = get_db_connection()
    if conn:
        print("Connection successful!")
        # ... perform database operations ...
        close_db_connection(conn)  # Important: close the connection
    else:
        print("Connection failed.")