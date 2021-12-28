






from db.clientSQL import clientSQL
import os

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
          if command.rstrip() != '':
            mysql.client.execute(command)
        except ValueError as msg:
            print("Command skipped: ", msg)

mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)

executeScriptsFromFile('/db/sql/backup/db.sql')
mysql.mydb.commit()


sql = "DELETE FROM User"
mysql.client.execute(sql)
mysql.mydb.commit()

# #Añador nuevos usuarios
sql = "INSERT INTO User (user_id,email,password,carddata) VALUES (%s,%s,%s,%s)"
val = [
    (1,"luiscaumel@gmail.com","password","0000-0000-0000-0000"),
    (2,"l.caumel@gmail.com","password","0000-0000-0000-0001")
]
mysql.client.executemany(sql,val)
mysql.mydb.commit()

