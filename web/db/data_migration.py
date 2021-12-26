from logging import exception
import os
from clientSQL import clientSQL
from client import DBClient
from bson.objectid import ObjectId


SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

NOSQL_URL = os.getenv("DDBB_NOSQL_URL","localhost")
NOSQL_PORT = os.getenv("DDBB_NOSQL_PORT",27017)
NOSQL_USER = os.getenv("DDBB_NOSQL_USER","admin")
NOSQL_PASS = os.getenv("DDBB_NOSQL_PASS","admin")
NOSQL_NAME = os.getenv("DDBB_NOSQL_NAME","db")
NOSQL_AUTH = os.getenv("DDBB_NOSQL_AUTHDB","admin")


mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)

clientM = DBClient(NOSQL_URL,NOSQL_NAME,NOSQL_USER,NOSQL_PASS,NOSQL_AUTH)

database = clientM.createDatabase("db")

clientM.clean_collection("Company")
clientM.clean_collection("Original_Game")
clientM.clean_collection("Genre")
clientM.clean_collection("User")
clientM.clean_collection("Library")
clientM.clean_collection("Community")
clientM.clean_collection("Game")
clientM.clean_collection("Review")

# colCompany = database["Company"]
# colOriginalGame = database["Original_game"]
# colGenre = database["Genre"]
# colUser = database["User"]
# colLibrary = database["Library"]
# colCommunity = database["Community"]
# colGame = database["Game"]
# colReview = database["Review"]
# print(database.list_collection_names())


columns = "*"
table = "Company"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
company = mysql.listToDict(columnName, data)

columns = "*"
table = "Genre"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
genre = mysql.listToDict(columnName, data)

columns = "*"
table = "Original_Game"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
original_game = mysql.listToDict(columnName, data)

columns = "*"
table = "Original_Game_Have_Genre"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
original_game_have_genre = mysql.listToDict(columnName, data)

columns = "*"
table = "User"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user = mysql.listToDict(columnName, data)

columns = "*"
table = "Library"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
library = mysql.listToDict(columnName, data)

columns = "*"
table = "Game"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
game = mysql.listToDict(columnName, data)

columns = "*"
table = "User_Buy_Original_Game"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user_buy_original_game = mysql.listToDict(columnName, data)

columns = "*"
table = "Community"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
community = mysql.listToDict(columnName, data)

columns = "*"
table = "User_Rate_Original_Game"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user_rate_original_game = mysql.listToDict(columnName, data)

columns = "*"
table = "User_Follow_User"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user_follow_user = mysql.listToDict(columnName, data)

columns = "*"
table = "User_Rate_Review"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user_rate_review = mysql.listToDict(columnName, data)

columns = "*"
table = "Review"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
review = mysql.listToDict(columnName, data)

columns = "*"
table = "User_Subscribe_Community"
columnName = mysql.getColumnNames(mysql.client,table)
data = mysql.select(mysql.client,columns,table)
user_subscribe_community = mysql.listToDict(columnName, data)

##Company

company_id = {}
for index,element in enumerate(company):
    del element["company_id"]
    result = clientM.insert_one("Company",element)
    company_id[index+1] = str(result.inserted_id)
print(company_id)

# Genre

genre_id = {}
for index,element in enumerate(genre):
    del element["genre_id"]
    result = clientM.insert_one("Genre",element)
    genre_id[index+1] = str(result.inserted_id)
print(genre_id)

# Original Game
original_game_id = {}
for index,element in enumerate(original_game):
    #Add company
    element["Company_id"] = company_id[element["Companycompany_id"]]
    del element["Companycompany_id"]
    #Add genre
    listGenre = []
    for elementGenre in original_game_have_genre:
        if elementGenre["Original_Gameoriginal_game_id"] == index + 1:
            listGenre.append(genre_id[elementGenre["Genregenre_id"]])
    element["GenreIds"] = listGenre
    del element["original_game_id"]
    #Add bbdd
    result = clientM.insert_one("Original_Game",element)
    original_game_id[index+1] = str(result.inserted_id)
print(original_game_id)

# User
user_id = {}
for index,element in enumerate(user):
    del element["user_id"]
    element["CommunityIds"] = []
    element["UserFriends"] = []
    result = clientM.insert_one("User",element)
    user_id[index+1] = str(result.inserted_id)
print(user_id)

#Company
community_id = {}
for index,element in enumerate(community):
    del element["community_id"]
    element["userCreator"] = str(user_id[element["Useruser_id"]])
    del element["Useruser_id"]
    result = clientM.insert_one("Community",element)
    community_id[index+1] = str(result.inserted_id)
print(community_id)

#Add user friend and community to user
for key,value in user_id.items():
    for index,element in enumerate(user_subscribe_community):
        if element["Useruser_id"] == key:
            clientM.update_one("User",{"_id":ObjectId(value)},{"CommunityIds":community_id[element["Communitycommunity_id"]]},"push")
    for index,element in enumerate(user_follow_user):
        if element["Useruser_id1"] == key:
            clientM.update_one("User",{"_id":ObjectId(value)},{"UserFriends":user_id[element["Useruser_id2"]]},"push")

# User
library_id = {}
for index,element in enumerate(library):
    del element["library_id"]
    element["userId"] = user_id[element["Useruser_id"]]
    del element["Useruser_id"]
    result = clientM.insert_one("Library",element)
    library_id[index+1] = str(result.inserted_id)
print(library_id)

#Game
game_id = {}
for index,element in enumerate(game):
    del element["game_id"]
    element["libraryId"] = library_id[element["Librarylibrary_id"]]
    del element["Librarylibrary_id"]
    element["OriginalGameId"] = original_game_id[element["Original_Gameoriginal_game_id"]]
    del element["Original_Gameoriginal_game_id"]
    element["date"] = element["date"].strftime('%Y-%m-%d')
    result = clientM.insert_one("Game",element)
    game_id[index+1] = str(result.inserted_id)
print(game_id)

#Review
review_id = {}
for index,element in enumerate(review):
    del element["review_id"]
    element["date"] = element["date"].strftime('%Y-%m-%d')
    element["userId"] = user_id[element["Useruser_id"]]
    del element["Useruser_id"]
    # if element["Original_Gameoriginal_game_id"]==None:
    #     print("asda")
    # elif element["Companycompany_id"]==None:
    #     print("asda2")
    try:
        element["OriginalGameId"] = original_game_id[element["Original_Gameoriginal_game_id"]]
    except Exception as e:
        element["OriginalGameId"] = None
    del element["Original_Gameoriginal_game_id"]
    try:
        element["CompanyId"] = original_game_id[element["Companycompany_id"]]
    except Exception as e:
        element["CompanyId"] = None
    del element["Companycompany_id"]
    result = clientM.insert_one("Review",element)
    review_id[index+1] = str(result.inserted_id)
print(review_id)


### falta la tabla de rate original game y company
### Falta la tabla subscrite community para la date
### tabla de user follow user (Añado el date como un diccionario ?)

#Change game buy user date, for buyDate 