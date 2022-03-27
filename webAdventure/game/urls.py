from django.urls import path
from . import views

# paths for the urls
urlpatterns = [
    path("", views.title),
    # you have to put world in the url, but this can be changed
    # when you click start, which should do that
    path("world", views.world)
]
