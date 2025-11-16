import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pasantren"
        )

        if connection.is_connected():
            print("Koneksi ke MySQL BERHASIL")
            return connection

    except Error as e:
        print("Error koneksi:", e)
        return None
