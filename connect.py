import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="javeriakashan.mysql.pythonanywhere-services.com",  # PythonAnywhere MySQL host
        user="javeriakashan",  # Your PythonAnywhere username
        database="javeriakashan$fms"  # Full database name
    )
    return connection
