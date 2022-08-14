from django.urls import path
from . import views


urlpatterns = [
    path("", views.signin, name="signin"),
    path("ranker/", views.machine, name="ranker"),
    path("logout/", views.logout_user, name="logout"),
]


