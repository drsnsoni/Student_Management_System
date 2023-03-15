from django.http import HttpResponse
from .models import Student
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import signupgorm
# Create your views here.
def index(request):
    students = Student.objects.all()
    context ={
        "stud" :students
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = signupgorm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signupgorm()

    context = {'form': form}
    return render(request, 'register.html', context)
    