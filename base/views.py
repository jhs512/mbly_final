import datetime

from django.http import HttpRequest
from django.shortcuts import render

from db_var.models import DbVar


def index(request: HttpRequest):
    DbVar.set('name', '홍길동', datetime.datetime.now() + datetime.timedelta(minutes=+30))
    print(DbVar.get('name', '하하'))
    #DbVar.remove('name')

    return render(request, "home/main.html")
