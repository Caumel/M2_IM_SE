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

def getColumnNames(client,tableName):
    columns = "*"
    client.execute(f"SELECT {columns} FROM {tableName}")
    columnNames = client.description
    result = client.fetchall()
    columnNames = [column[0] for column in columnNames]
    return columnNames 

def select(client,columns,table):
    client.execute(f"SELECT {columns} FROM {table}")
    result = client.fetchall()
    result = [list(row) for row in result]
    return result

def selectWhere(client,columns, table, where):
    client.execute(f"SELECT {columns} FROM {table} WHERE {where}")
    result = client.fetchall()
    result = [list(row) for row in result]
    return result

def selectOrder(client, columns, table, order):
    client.execute(f"SELECT {columns} FROM {table} ORDER BY {order}")
    result = client.fetchall()
    result = [list(row) for row in result]
    return result

def selectOrderDesc(client, columns, table, order):
    client.execute(f"SELECT {columns} FROM {table} ORDER BY {order} DESC")
    result = client.fetchall()
    result = [list(row) for row in result]
    return result

def selectWhereOrder(client,columns, table, where, order):
    client.execute(f"SELECT {columns} FROM {table} WHERE {where} ORDER BY {order}")
    result = client.fetchall()
    result = [list(row) for row in result]
    return result

def listToDict(columnName, data):
    listMongo = []
    for row in data:
        dictRow = {}
        for index, column in enumerate(columnName):
            dictRow[column] = row[index]
        listMongo.append(dictRow)
    return listMongo


columns = "*"
table = "Company"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
company = listToDict(columnName, data)

columns = "*"
table = "Genre"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
genre = listToDict(columnName, data)

columns = "*"
table = "Original_Game"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
original_game = listToDict(columnName, data)

columns = "*"
table = "Original_Game_Have_Genre"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
original_game_have_genre = listToDict(columnName, data)

columns = "*"
table = "User"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user = listToDict(columnName, data)

columns = "*"
table = "Library"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
library = listToDict(columnName, data)

columns = "*"
table = "Game"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
game = listToDict(columnName, data)

columns = "*"
table = "User_Buy_Original_Game"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user_buy_original_game = listToDict(columnName, data)

columns = "*"
table = "Community"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
community = listToDict(columnName, data)

columns = "*"
table = "User_Rate_Original_Game"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user_rate_original_game = listToDict(columnName, data)

columns = "*"
table = "User_Follow_User"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user_follow_user = listToDict(columnName, data)

columns = "*"
table = "User_Rate_Review"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user_rate_review = listToDict(columnName, data)

columns = "*"
table = "Review"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
review = listToDict(columnName, data)

columns = "*"
table = "User_Subscribe_Community"
columnName = getColumnNames(client,table)
data = select(client,columns,table)
user_subscribe_community = listToDict(columnName, data)


##Company

lista = [company]
lista = [original_game,original_game_have_genre,genre]
lista = [genre]
lista = [user,community,user_subscribe_community]
lista = [library,user]
lista = [community,user]
lista = [game,library,original_game]
lista = [review,original_game,company,user]