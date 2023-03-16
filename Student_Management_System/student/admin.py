from django.contrib import admin
from .models import Student, department, Exam, Subject, Marks
# Register your models here.
admin.site.register(Student)
admin.site.register(department)
admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Marks)
