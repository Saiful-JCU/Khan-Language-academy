from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            print(form)
            print("hello")
    return render(request, 'register/register.html', {'form':form})