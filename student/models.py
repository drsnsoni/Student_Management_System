from django.db import models

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
    cource = models.ForeignKey(Course, blank=True,default=1, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, blank=True, default='1',on_delete=models.CASCADE)
    studying = models.BooleanField(default=1)

    def __str__(self):
        return str(self.Enroll_no)

#activity model
class Activity(models.Model):
    activity_title = models.TextField()
    activity_file = models.ImageField(upload_to='static/activity')
    enroll_no = models.IntegerField()
    def __str__(self):
        return str(self.enroll_no) + ' (' + str(self.activity_title)+ ')'

#assignment table
class Assignment(models.Model):
    assignment_title = models.TextField()
    assignment_file = models.ImageField(upload_to='static/assignment')
    enroll_no = models.IntegerField()
    def __str__(self):
        return str(self.enroll_no) + ' (' + str(self.assignment_title)+ ')'



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

    def __str__(self):
        return self.name

#result
class StudentResult(models.Model):
    enroll_no = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return str(self.student)

#notifications model
class Notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/notification', blank=True)
    date = models.DateField()
    def __str__(self):
        return self.title

#for student buy    
class Store(models.Model):
    title = models.CharField(max_length=100)
    TSHIRT_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'Other'),
    ]
    size = models.CharField(choices=TSHIRT_CHOICES, max_length=20)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

#products of college
class Products(models.Model):
    name = models.CharField(max_length=100)
    available_size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products', blank=True)
    def __str__(self):
        return self.name
    
#upcoming Events 
class Upcoming(models.Model):
    event_name = models.CharField(max_length=200)
    event_link = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    event_banner = models.ImageField(blank=True, upload_to='static/event')
    event_date  = models.DateField()
    def __str__(self):
        return self.event_name
    
#attendance 
class Attendance(models.Model):
    enroll_no = models.IntegerField()
    year_day = models.IntegerField()
    last_date = models.DateField()
    def __str__(self):
        return str(self.enroll_no)