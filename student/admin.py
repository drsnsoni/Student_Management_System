from django.contrib import admin
from.models import Student,Course,Department,AcadamicInfo,Subject,Exam,StudentResult
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(AcadamicInfo)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(StudentResult)