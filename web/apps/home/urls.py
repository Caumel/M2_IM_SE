# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [


    path('actionUrl',views.importSQL, name='actionUrl'),
    path('migrationUrl',views.migrationMethod, name='migrationUrl'),
    # The home page
    path('', views.index, name='home'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
