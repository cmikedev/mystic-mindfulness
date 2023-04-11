from django.shortcuts import render
from .models import *
import random


def index(request):
    """ A view to return the index page and random quotes """

    #quotes = list(Quote.objects.all())
    #quotes = random.sample(quotes, 3)

    quotes = Quote.objects.all()
    quotes = Quote.objects.order_by('?')[:1]

    context = {
        'quotes': quotes,
    }

    return render(request, 'home/index.html', context)
