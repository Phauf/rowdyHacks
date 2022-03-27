from curses import keyname
from multiprocessing import Event
from optparse import TitledHelpFormatter
from tkinter.tix import DisplayStyle
from turtle import onkey, onkeypress, onkeyrelease
from django.shortcuts import render

from django import forms

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  # i think these are not needed
from django.template import loader  # i think these are not needed

# there will be images with same format in the visual value
# more dictionary values will be added
# 49 more...
welcome = [
    {'visual': "img-6-3", 'title': "Starting out", 'description': "Here is a long description for the page",
        'yousee': ['stick', 'map', 'potion']
     },
    {
        'visual': "img-6-2", 'title': "The Wrestling room", 'description': "I DON'T WANT TO TYPE ANYMORE", 'yousee': ['sword', 'chair', 'enemy']
    },
    {
        'title': "The Room", 'description': "A strange futuristic vibe fills the room", 'yousee': ['monitor', 'table', 'computer']
    }
]


class NewTaskForm(forms.Form):
    terminal = forms.CharField(label=">")


# This will show the title.html page
def title(request):
    return render(request, "game/title.html")


def world(request):
    # This should be checked
    # welcome[changeMeDependingOnPosition][0]
    # welcome[changeMeDependingOnPosition][1]
    # welcome[changeMeDependingOnPosition][2]
    visual = welcome[0]['visual']
    title = welcome[0]['title']
    description = welcome[0]['description']
    yousee = welcome[0]['yousee']

# These are the variables that are sent to the html document
    context = {
        "visual": visual,
        "title": title,
        "description": description,
        "yousee": yousee,
        "terminal": NewTaskForm()
    }
    return render(request, "game/world.html", context)


def battle(request):
    # logic for the

    return render(request, 'game/battle.html')
