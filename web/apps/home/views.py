# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
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

PRINT = False

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
    global PRINT
    if PRINT:
        print("asda")
    PRINT = True

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

    context = {'segment': 'index'}
    html_template = loader.get_template('home/dashboard.html')

    return redirect(request.META['HTTP_REFERER'])

def migrationMethod(request):
    global PRINT
    if PRINT:
        print("asda")
    migration = migrationNoSQL()
    migration.cleanDatabase(migration.clientM)
    migration.importDataMongo()

    context = {'segment': 'index'}
    html_template = loader.get_template('home/dashboard.html')

    return redirect(request.META['HTTP_REFERER'])

def caseUse1():

    query = "SELECT ULGame.price, Original_Game.name, ULGame.refounded, ULGame.`date`, Original_Game.rating FROM (SELECT UserLibrary.email, Game.price, Game.refounded, Game.`date`, Game.Original_Gameoriginal_game_id FROM (SELECT User.email, User.password, User.carddata, Library.number_of_games, Library.library_id FROM User LEFT JOIN Library ON User.user_id = Library.library_id WHERE User.email = 'luiscaumel@gmail.com') AS UserLibrary LEFT JOIN Game ON UserLibrary.library_id = Game.Librarylibrary_id ORDER BY price DESC) AS ULGame LEFT JOIN Original_Game ON ULGame.Original_Gameoriginal_game_id = Original_Game.original_game_id"
    mysql.client.execute(query)
    columnNames = mysql.client.description
    print(columnNames)
    result = mysql.client.fetchall()
    result = [list(row) for row in result]
    print(result)

def useCase1NoSQL(request):
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
    resultList = []
    for i in result:
        resultList.append(i)
    print(resultList)

    context = {
        'resultList': resultList,
        'column': resultList[0].keys()
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