from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import SignUpForm, StudentForm, activityform, assignmentform
from .models import Student, StudentResult,Activity,Assignment
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
            
            stu = Student.objects.filter(Enroll_no=int(username))
            if len(stu)>0:
                return redirect('dashboard/'+ username)  
            else:
                return redirect('personalinfo')
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
    stud_data = Student.objects.get(Enroll_no = id)
    context={
        'student':stud,
        'stud_data':stud_data
    }
   
    return render(request, 'dashboard.html', context)
   

@login_required(login_url='/login')
def result(request):
    result = StudentResult.objects.all()
    context = {
        'result' : result
    }
    return render(request, 'results.html', context)

@login_required(login_url='/login')
def activity(request):
    if request.method == 'POST':
        form = activityform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity')
            # redirect to success page
    else:
     form = activityform()  
    user = request.user
    act = Activity.objects.filter(enroll_no=str(user))
    return render(request,'activity.html', {'form': form, 'activity':act})


@login_required(login_url='/login')
def assignment(request):
    if request.method == 'POST':
        form = assignmentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assignments')
            # redirect to success page
    else:
     form = assignmentform()  
    user = request.user
    asign= Assignment.objects.filter(enroll_no=str(user))
    return render(request, 'assignments.html',{'form': form, 'asign':asign})

@login_required(login_url='/login')
def profile(request):
   if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
            # redirect to success page
   else:
     form = StudentForm()
   return render(request, 'profile.html', {'form': form})

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    request.session['user']=False
    return redirect('login')
