from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  # i think these are not needed
from django.template import loader  # i think these are not needed

welcome = [
    {'title': "Starting out", 'description': "Here is a long description for the page",
        'yousee': ['stick', 'map', 'potion']
     },
    {
        'title': "The Wrestling room", 'description': "I DON'T WANT TO TYPE ANYMORE", 'yousee': ['sword', 'chair', 'enemy']
    },
    {
        'title': "The Room", 'description': "A strange futuristic vibe fills the room", 'yousee': ['monitor', 'table', 'computer']
    }
]

print(welcome[2]['title'] + "\n" + welcome[2]
      ['description'] + "\n>You see: \n" + ', '.join(welcome[2]['yousee']))


# this will
def title(request):
    return render(request, "game/title.html", )


def some(request):
    return render(request, )
