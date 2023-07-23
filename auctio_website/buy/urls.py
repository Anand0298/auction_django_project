from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("watchlist/<str:username>", views.watchlistpage, name = "watchlist"),
   path("watchlist",views.addwatch,name="addwatchlist"),
   path("delete", views.deletewatch, name = "deletewatch"),
   path("winner", views.winner, name="winner"),
   path("winnings", views.winnings, name="winnings"),
]
