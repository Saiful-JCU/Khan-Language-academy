from django.urls import path 
from academy.views import home

urlpatterns = [
    path("", home )
]