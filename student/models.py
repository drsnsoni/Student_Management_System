from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Enroll_no = models.IntegerField()
    date_of_birth = models.DateField()
    SPI = models.DecimalField(max_digits=3, decimal_places=2)
    CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    adhar_no = models.IntegerField()
    sem = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'Other'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    mobile_no = models.IntegerField()
    parents_no = models.IntegerField()
    parents_email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

   

class Course(models.Model):
    course_name = models.TextField()
    def __str__(self):
        return self.course_name

class Department(models.Model):
    department_name = models.TextField()
    def __str__(self):
        return self.department_name

   

class AcadamicInfo(models.Model):
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.BooleanField()
    def __str__(self):
        return self.Student_id

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Enroll(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment = models.IntegerField(unique=True)

class StudentResult(models.Model):

    student = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return str(self.student) + '(' + str(self.exam)+ ')'
