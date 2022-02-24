import logging

from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    print("메인")
    return render(request, "home/main.html")
