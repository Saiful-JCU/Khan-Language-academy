from django.urls import path 
from academy.views import home, todaysTask

urlpatterns = [
    path("", home ),
    path("todaystask/", todaysTask , name="todaystask"),
]