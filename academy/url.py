from django.urls import path 
from academy.views import home, todaysTask,  add_all_data, success 

urlpatterns = [
    path("", home ),
    path("todaystask/", todaysTask , name="todaystask"),
    # path('createTask/', createTask, name='createTask'), 
    path("add-all/", add_all_data, name="add_all"),
    path("success/", success, name="success_page")

]