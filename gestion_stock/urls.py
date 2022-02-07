from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
     path('pp', views.pop,name="pop"),
      path('lkr', views.lekhr,name="lekher"),
      path("<str:name>",views.nom,name="nom"),
]
