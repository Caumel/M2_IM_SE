# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import db, template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render




from db.clientSQL import clientSQL
from db.client import DBClient

from db.data_migration import migrationNoSQL

import os
import time

kindDB = "SQL"

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)

NOSQL_URL = os.getenv("DDBB_NOSQL_URL","localhost")
NOSQL_PORT = os.getenv("DDBB_NOSQL_PORT",27017)
NOSQL_USER = os.getenv("DDBB_NOSQL_USER","admin")
NOSQL_PASS = os.getenv("DDBB_NOSQL_PASS","admin")
NOSQL_NAME = os.getenv("DDBB_NOSQL_NAME","db")
NOSQL_AUTH = os.getenv("DDBB_NOSQL_AUTHDB","admin")

clientM = DBClient(NOSQL_URL,NOSQL_NAME,NOSQL_USER,NOSQL_PASS,NOSQL_AUTH)

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

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

def importSQL(request):
    global kindDB
    kindDB = "SQL"

    executeScriptsFromFile('/db/sql/backup/db.sql')
    mysql.mydb.commit()

    sql = "DELETE FROM User WHERE email = 'l.caumel@gmail.com'"
    mysql.client.execute(sql)
    mysql.mydb.commit()

    # #Añador nuevos usuarios
    sql = "INSERT INTO User (user_id,email,password,carddata) VALUES (%s,%s,%s,%s)"
    val = [
        (2,"l.caumel@gmail.com","password","0000-0000-0000-0001")
    ]
    mysql.client.executemany(sql,val)
    mysql.mydb.commit()

    time.sleep(2)

    context = {'segment': 'index'}
    html_template = loader.get_template('home/dashboard.html')

    return redirect(request.META['HTTP_REFERER'])

def migrationMethod(request):

    global kindDB
    kindDB = "NoSQL"
    

    migration = migrationNoSQL()
    migration.cleanDatabase(migration.clientM)
    migration.importDataMongo()

    time.sleep(2)

    context = {'segment': 'index'}
    html_template = loader.get_template('home/dashboard.html')

    return redirect(request.META['HTTP_REFERER'])

def useCase1NoSQL(request):

    global kindDB

    if kindDB == "SQL":
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
        
    
    elif kindDB == "NoSQL":
        pipeline = [{
                "$lookup":
                    {
                        "from":"Library",
                        "localField": "libraryId",
                        "foreignField": "_id",
                        "as": "library"
                    }
            },
            {
                "$unwind":"$library"
            },
            {
                "$project":
                    {   
                        "price":1,
                        "refounded":1,
                        "date":1,
                        "OriginalGameId":1,
                        "number_of_games": "$library.number_of_games",
                        "userId": "$library.userId",
                    }
            },
            {
                "$lookup":
                    {
                        "from":"Original_Game",
                        "localField": "OriginalGameId",
                        "foreignField": "_id",
                        "as": "OriginalGame"
                    }
            },
            {
                "$unwind":"$OriginalGame"
            },
            {
                "$project":
                    {
                        "Name": "$OriginalGame.name",
                        "Rating": "$OriginalGame.rating",
                        "price":1,
                        "refounded":1,
                        "date":1,
                        "userId": 1,
                    }
            },
            {
                "$lookup":
                    {
                        "from":"User",
                        "localField": "userId",
                        "foreignField": "_id",
                        "as": "user"
                    }
            },
            {
                "$unwind":"$user"
            },
            {
                "$project":
                    {
                        "_id":0,
                        "Name": 1,
                        "Rating": 1,
                        "price":1,
                        "refounded":1,
                        "date":1,
                        "email": "$user.email",
                    }
            },
            {
                "$match": {"email":"luiscaumel@gmail.com"},
            },
            {
                "$sort":{"price": -1}
            }]
        result = clientM.client["db"]["Game"].aggregate(pipeline)
        result_dict = []
        for i in result:
            i["Kind"] = "NoSQL"
            result_dict.append(i)

    print(result_dict)
    context = {
        'resultList': result_dict,
        }

    return render(request, 'home/reportLuis.html', context)



"""
SELECT  ULGame.price, Original_Game.name, ULGame.refounded, ULGame.`date`, Original_Game.rating
FROM (
        SELECT UserLibrary.email, Game.price, Game.refounded, Game.`date`, Game.Original_Gameoriginal_game_id 
        FROM (
                SELECT User.email, User.password, User.carddata, Library.number_of_games, Library.library_id 
                FROM User 
                LEFT JOIN Library 
                ON User.user_id = Library.library_id
                WHERE User.email = 'luiscaumel@gmail.com'
            ) 
        AS UserLibrary
        LEFT JOIN Game
        ON UserLibrary.library_id = Game.Librarylibrary_id
        ORDER BY price DESC
    ) 
AS ULGame
LEFT JOIN Original_Game
ON ULGame.Original_Gameoriginal_game_id = Original_Game.original_game_id
"""

"""
db.Game.aggregate([
    {
        $lookup:
            {
                from:"Library",
                localField: "libraryId",
                foreignField: "_id",
                as: "library"
            }
    },
    {
        "$unwind":"$library"
    },
    {
        $project:
            {   
                price:1,
                refounded:1,
                date:1,
                OriginalGameId:1,
                number_of_games: "$library.number_of_games",
                userId: "$library.userId",
            }
    },
    {
        $lookup:
            {
                from:"Original_Game",
                localField: "OriginalGameId",
                foreignField: "_id",
                as: "OriginalGame"
            }
    },
    {
        "$unwind":"$OriginalGame"
    },
    {
        $project:
            {
                Name: "$OriginalGame.name",
                Rating: "$OriginalGame.rating",
                price:1,
                refounded:1,
                date:1,
                number_of_games:1,
                userId: 1,
            }
    },
    {
        $lookup:
            {
                from:"User",
                localField: "userId",
                foreignField: "_id",
                as: "user"
            }
    },
    {
        "$unwind":"$user"
    },
    {
        $project:
            {
                _id:0,
                Name: 1,
                Rating: 1,
                price:1,
                refounded:1,
                date:1,
                number_of_games:1,
                email: "$user.email",
            }
    },
    {
        $match: {"email":"luiscaumel@gmail.com"},
    },
    {
        $sort:{"price": -1}
    }
])
"""