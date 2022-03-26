from django.urls import path
from . import views

#paths for the urls
urlpatterns = [
    path("", views.title)
]