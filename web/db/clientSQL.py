import mysql.connector
import os

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")


mydb = mysql.connector.connect(
    user=SQL_USER,
    password=SQL_PASS,
    host=SQL_URL,
    port=SQL_PORT,
    database=SQL_NAME,
)

client = mydb.cursor()

client.execute("SELECT * FROM User")