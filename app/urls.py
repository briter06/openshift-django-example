from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="App-index"),
    path('add', views.add_persona, name="Add-index")
]