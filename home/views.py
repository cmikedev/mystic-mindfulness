from django.shortcuts import render
from .models import *


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
