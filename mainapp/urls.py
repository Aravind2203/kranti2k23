from django.urls import path
from .views import *
urlpatterns = [
    path("register-solo",registerSolo),
    path("register-team",registerTeam)
]