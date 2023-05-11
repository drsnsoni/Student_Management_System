from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import SignUpForm, StudentForm
from .models import Student, StudentResult
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            # return redirect('dashboard/'+ username)
            return redirect('dashboard/'+username)
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # redirect to success page
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'signup.html', context)


@login_required(login_url='/login')
def dashboard(request, id):
    stud = User.objects.get(username=id)
  
    context={
        'student':stud,
       
    }
    return render(request, 'dashboard.html', context)

# @login_required(login_url='/login')  
# def studnt(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'fillform.html', {'form': form})  
#         else:
#             return redirect('login')
        


@login_required(login_url='/login')
def result(request):
    result = StudentResult.objects.all()
    context = {
        'result' : result
    }
    return render(request, 'results.html', context)

@login_required(login_url='/login')
def activity(request):
    return render(request, 'activity.html')

@login_required(login_url='/login')
def attendance(request, id):
    
    result = StudentResult.objects.get(student=id)
    
    return render(request, 'attendance.html')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    request.session['user']=False
    return redirect('login')
