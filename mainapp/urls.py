from django.urls import path
from .views import *
urlpatterns = [
    path("reg-solo.html",registerSolo),
    path("reg-team.html",registerTeam),
    path("reg-fifa.html",registerFifa),
    path("reg_cod.html",registerCod),
    path("reg_valo.html",registerValo),
    path("",index),
    path("home.html",home),
    path("event-tagline.html",eventTagline),
    path("photomania.html",photomania),
    path("geekspeak.html",geekspeak),
    path("algolia.html",algolia),
    path("codehunt.html",codehunt),
    path("sharktank.html",sharktank),
    path("s2s.html",s2s),
    path("connexions.html",connexions),
    path("techtonic.html",techtonic),
    path("gaming-events.html",gamingevent),
    path("fifa.html",fifa),
    path("valorant.html",valorant),
    path("cod.html",cod)
]