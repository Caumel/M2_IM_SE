from db.clientSQL import clientSQL
from db.client import DBClient

from db.data_migration import migrationNoSQL

import os
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)


date = (datetime.now() - relativedelta(years=1)).strftime("%Y-%m-%d")
date2 = datetime.now().strftime("%Y-%m-%d")
print(date,date2)
userString = "luiscaumel@gmail.com"
query = f"SELECT ULGame.price, Original_Game.name, ULGame.refounded, ULGame.`date`, Original_Game.rating, ULGame.email FROM (SELECT UserLibrary.email, Game.price, Game.refounded, Game.`date`, Game.Original_Gameoriginal_game_id FROM (SELECT User.email, User.password, User.carddata, Library.number_of_games, Library.library_id FROM User LEFT JOIN Library ON User.user_id = Library.library_id WHERE User.email = '{userString}') AS UserLibrary LEFT JOIN Game ON UserLibrary.library_id = Game.Librarylibrary_id ORDER BY price DESC) AS ULGame LEFT JOIN Original_Game ON ULGame.Original_Gameoriginal_game_id = Original_Game.original_game_id WHERE ULGame.`date` BETWEEN '{date}' AND '{date2}' ORDER BY ULGame.price DESC"
mysql.client.execute(query)
result = mysql.client.fetchall()