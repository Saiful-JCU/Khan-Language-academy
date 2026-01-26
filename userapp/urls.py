from django.contrib import admin
from django.urls import path
from userapp.views import sign_in, sign_up


urlpatterns = [
    path('',  sign_in, name="sign-in"),
    path('register/',  sign_up, name="sign_up")
]

