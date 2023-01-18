from django.shortcuts import render

from .app import *


def index(request):
    return render(request, "hcc/dashboard.html", None)
