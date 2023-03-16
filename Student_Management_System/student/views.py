from django.http import HttpResponse
from .models import Student
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import signupgorm
from django.contrib.auth import logout
# Create your views here.
def index(request):
    students = Student.objects.all()
    context ={
        "stud" :students
    }
    return render(request, 'index.html', context)

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'dashboard.html')
        else:
            # result = render(request, "login.html")
            # message = "Wrong USername Or Password"
            # if result:
            #     context = {
            #         "message":message
            #     }
            return render(request, 'login.html')
    else:
        return render(request, "login.html")

   
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
    

def activity(request):
    return render(request, 'activities.html')

def result(request):
    return render(request, 'results.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')