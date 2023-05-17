from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import SignUpForm, StudentForm, activityform, assignmentform
from .models import Student, StudentResult,Activity,Assignment, Notification, Products, Attendance, Upcoming
from django.contrib.auth.models import User

def base(name):
    #attendance
    total_days = 365  # Total number of days
    attended_days = Attendance.objects.filter(enroll_no=str(name))
    final= str(attended_days.values("year_day")[0]['year_day'])
    attendance_percentage = (int(final) / total_days) * 100
    percentage = int(attendance_percentage)

    if attended_days=='':
        percentage="Not Found"
    #cgpa
    cgpa = Student.objects.filter(Enroll_no=str(name))
    cgpa2 = int(cgpa.values('CGPA')[0]['CGPA'])
    #progress
    if cgpa2 > 7:
        progress = "Nice Great"
    elif cgpa < 5:
        progress = "Good"
    else:
        progress = "work Hard"
    #total students
    total_student = Student.objects.all()
    count = total_student.count()

    return {'cgpa': cgpa2, 'total_student':count, 'percentage':percentage, 'progress': progress}



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
    user = request.user
    basic=base(user)
    context={
        'student':stud,
        'stud_data':stud_data,
        'basic':basic,
    }
   
    return render(request, 'dashboard.html', context)
   

@login_required(login_url='/login')
def result(request):
    user = request.user
    basic=base(user)
    result = StudentResult.objects.filter(enroll_no=str(user))
    print(result)
    context = {
        'result' : result,
        'basic':basic,
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
   
    basic=base(user)
    act = Activity.objects.filter(enroll_no=str(user))
    return render(request,'activity.html', {'form': form, 'activity':act, 'basic':basic})


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
    basic=base(user)
    asign= Assignment.objects.filter(enroll_no=str(user))
    return render(request, 'assignments.html',{'form': form, 'asign':asign, 'basic':basic})

@login_required(login_url='/login')
def profile(request):
   if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personalinfo')
            # redirect to success page
   else:
     form = StudentForm()
     user = request.user
    
   return render(request, 'profile.html', {'form': form, })

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    request.session['user']=False
    return redirect('login')

@login_required(login_url='/login')
def notification(request):
   user = request.user
   basic=base(user)
   notify = Notification.objects.all()
   return render(request, 'notification.html', {'notify':notify, 'basic':basic})

@login_required(login_url='/login')
def store(request):
   #for Attandance
   user = request.user
   basic=base(user)
   product = Products.objects.all()
   return render(request, 'store.html', {'product':product, 'basic':basic})

@login_required(login_url='/login')
def upcoming(request):
    user = request.user
    basic=base(user)
    upcoming = Upcoming.objects.all()
    return render(request, 'upcoming.html', {'basic':basic, 'upcoming':upcoming})

