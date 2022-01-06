    
from clientSQL import clientSQL
from client import DBClient

import os

PRINT = "SQL"

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)

    
query = "SELECT ULGame.price, Original_Game.name, ULGame.refounded, ULGame.`date`, Original_Game.rating, ULGame.email FROM (SELECT UserLibrary.email, Game.price, Game.refounded, Game.`date`, Game.Original_Gameoriginal_game_id FROM (SELECT User.email, User.password, User.carddata, Library.number_of_games, Library.library_id FROM User LEFT JOIN Library ON User.user_id = Library.library_id WHERE User.email = 'luiscaumel@gmail.com') AS UserLibrary LEFT JOIN Game ON UserLibrary.library_id = Game.Librarylibrary_id ORDER BY price DESC) AS ULGame LEFT JOIN Original_Game ON ULGame.Original_Gameoriginal_game_id = Original_Game.original_game_id"
mysql.client.execute(query)
result = mysql.client.fetchall()
result = [list(row) for row in result]
result_dict = []
for i in result:
    game = {}
    game["Name"] = i[1]
    game["price"] = i[0]
    game["Rating"] = i[4]
    game["date"] = i[3].strftime("%Y-%m-%d")
    if i[2]==0:
        game["refounded"] = False
    else:
        game["refounded"] = True
    game["email"] = i[5]
    game["Kind"] = "SQL"
    result_dict.append(game)