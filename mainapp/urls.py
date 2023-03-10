from django.urls import path
from .views import *
urlpatterns = [
    path("register-solo",registerSolo),
    path("register-team",registerTeam),
    path("register-fifa",registerFifa),
    path("register-cod",registerCod),
    path("register-valo",registerValo),
    path("",index),
    path("home.html",home),
    path("event-tagline.html",eventTagline),
]