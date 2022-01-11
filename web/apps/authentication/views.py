# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User

from db.clientSQL import clientSQL
import os

SQL_URL = os.getenv("DDBB_SQL_URL","localhost")
SQL_PORT = os.getenv("DDBB_SQL_PORT",3306)
SQL_USER = os.getenv("DDBB_SQL_USER","user")
SQL_PASS = os.getenv("DDBB_SQL_PASS","password")
SQL_NAME = os.getenv("DDBB_SQL_NAME","db")

mysql = clientSQL(SQL_USER,SQL_PASS,SQL_URL,SQL_PORT,SQL_NAME)


def login_view(request):
    try:
        user = User.objects.create_user('luiscaumel@gmail.com', 'luiscaumel@gmail.com', 'password1111')
        sql = "INSERT INTO User (user_id,email,password,carddata) VALUES (%s,%s,%s,%s)"
        val = [
            (1,"luiscaumel@gmail.com","password","0000-0000-0000-0000")
        ]
        mysql.client.executemany(sql,val)
        mysql.mydb.commit()
    except:
        print("Usuarios ya en base de datos")

    form = LoginForm(request.POST or None)


    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            sql = f"SELECT User.email, User.password FROM User WHERE User.email = '{username}'"
            mysql.client.execute(sql)
            result = mysql.client.fetchall()
            user = authenticate(username=username, password=password)
            if user is not None and result != []:
                login(request, user)
                return redirect("/dashboard.html")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

number = 2

def register_user(request):
    global number
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            carddata = form.cleaned_data.get("carddata")

            sql = "INSERT INTO User (user_id,email,password,carddata) VALUES (%s,%s,%s,%s)"
            val = [
                (number + 1,email,raw_password,carddata)
            ]
            number += 1
            mysql.client.executemany(sql,val)
            mysql.mydb.commit()

            print(email,carddata,raw_password)
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
