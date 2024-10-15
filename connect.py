import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",        # Change this for PythonAnywhere MySQL host
        user="your_username",
        password="your_password",
        database="fms"
    )
    return connection
