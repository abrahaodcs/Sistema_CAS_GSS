import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hinata@82',
    'database': 'cas_gss'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn
