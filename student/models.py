from django.db import models


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='static/profile_photos', default=False)
    email = models.EmailField()
    Enroll_no = models.IntegerField()
    date_of_birth = models.DateField()
    SPI = models.DecimalField(max_digits=3, decimal_places=2)
    CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'Other'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    mobile_no = models.IntegerField()
    parents_no = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

#activity model
class Activity(models.Model):
    activity_title = models.TextField()
    activity_file = models.ImageField(upload_to='static/activity')
    enroll_no = models.IntegerField()

#assignment table
class Assignment(models.Model):
    assignment_title = models.TextField()
    assignment_file = models.ImageField(upload_to='static/assignment')
    enroll_no = models.IntegerField()

#course model
class Course(models.Model):
    course_name = models.TextField()
    def __str__(self):
        return self.course_name
    
#Department Model
class Department(models.Model):
    department_name = models.TextField()
    def __str__(self):
        return self.department_name

#Acadamicinfo Model
class AcadamicInfo(models.Model):
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.BooleanField()
    def __str__(self):
        return self.Student_id

#exam model
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.name

#subject Model    
class Subject(models.Model):
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#Enroll number
class Enroll(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment = models.IntegerField(unique=True)

#result
class StudentResult(models.Model):
    student = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return str(self.student) + '(' + str(self.exam)+ ')'

