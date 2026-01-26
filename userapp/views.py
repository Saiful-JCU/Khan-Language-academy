from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_in(request):
    return render(request, 'registration/sign-in.html')

def sign_up(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    return render(request, 'registration/sign-up.html', {'form':form})