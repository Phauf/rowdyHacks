from curses import keyname
from multiprocessing import Event
from optparse import TitledHelpFormatter
from re import L
from tkinter.tix import DisplayStyle
from turtle import onkey, onkeypress, onkeyrelease
from django.shortcuts import render

import random
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
        'visual': "img-6-1", 'title': "The Room", 'description': "A strange futuristic vibe fills the room", 'yousee': ['monitor', 'table', 'computer']
    },
    {
        'visual': "img-enemy", 'title': "An enemy approaches", 'description': "You find it astonishing that there are still monsterous beasts roaming the lands", 'yousee': ["enemy"]
    },
    {
        'visual': "img-key", 'title': "An objects shines", 'description': "you traverse the maladroit path and see something catch your eye", 'yousee': ["key"]
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
    {
        'visual': "", 'title': "", 'description': "", 'yousee': ""
    },
]


class NewTaskForm(forms.Form):
    terminal = forms.CharField(label=">")

    def clean_terminal(self):
        data = self.clean_terminal["terminal"]
        return data


# This will show the title.html page
def title(request):
    return render(request, "game/title.html")


def world(request):
    # This should be checked
    # welcome[changeMeDependingOnPosition][0]
    # welcome[changeMeDependingOnPosition][1]
    # welcome[changeMeDependingOnPosition][2]
    visual = welcome[4]['visual']
    title = welcome[4]['title']
    description = welcome[4]['description']
    yousee = welcome[4]['yousee']

# These are the variables that are sent to the html document
    context = {
        "visual": visual,
        "title": title,
        "description": description,
        "yousee": yousee,
        "terminal": NewTaskForm(),
    }
    return render(request, "game/world.html", context)


def battle(request):
    # button stuff for the gifs
    roll = 'false'
    rolled = random
    context = {
        "roll": roll
    }
    return render(request, 'game/battle.html')
