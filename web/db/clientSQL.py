import mysql.connector
class clientSQL:
    def __init__(self,user,password,host,port,database):
        self.mydb = mysql.connector.connect(
                        user=user,
                        password=password,
                        host=host,
                        port=port,
                        database=database,
                    )
        self.client = self.mydb.cursor()
    
    def setClient(self, client):
        self.client = client

    def close(self):
        self.client.close()

    def cursor(self):
        self.client = self.mydb.cursor()

    def getColumnNames(self,client,tableName):
        columns = "*"
        client.execute(f"SELECT {columns} FROM {tableName}")
        columnNames = client.description
        result = client.fetchall()
        columnNames = [column[0] for column in columnNames]
        return columnNames 

    def select(self,client,columns,table):
        client.execute(f"SELECT {columns} FROM {table}")
        result = client.fetchall()
        result = [list(row) for row in result]
        return result

    def selectWhere(self,client,columns, table, where):
        client.execute(f"SELECT {columns} FROM {table} WHERE {where}")
        result = client.fetchall()
        result = [list(row) for row in result]
        return result

    def selectOrder(self,client, columns, table, order):
        client.execute(f"SELECT {columns} FROM {table} ORDER BY {order}")
        result = client.fetchall()
        result = [list(row) for row in result]
        return result

    def selectOrderDesc(self, client, columns, table, order):
        client.execute(f"SELECT {columns} FROM {table} ORDER BY {order} DESC")
        result = client.fetchall()
        result = [list(row) for row in result]
        return result

    def selectWhereOrder(self, client,columns, table, where, order):
        client.execute(f"SELECT {columns} FROM {table} WHERE {where} ORDER BY {order}")
        result = client.fetchall()
        result = [list(row) for row in result]
        return result

    def listToDict(self, columnName, data):
        listMongo = []
        for row in data:
            dictRow = {}
            for index, column in enumerate(columnName):
                dictRow[column] = row[index]
            listMongo.append(dictRow)
        return listMongo