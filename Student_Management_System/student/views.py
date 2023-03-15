from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    context ={
        "stud" :students
    }
    return render(request, 'index.html', context)