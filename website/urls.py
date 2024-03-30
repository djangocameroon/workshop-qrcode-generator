from django.urls import path

from website.views.workshop import generate, home

urlpatterns = [
    path("", home, name="home"),
    path("generate/", generate, name="generate"),
]
