from django.db import models

# Create your models here.

class department(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    profile_photo = models.ImageField(upload_to='students_profile')
    name = models.CharField(max_length=50)
    enroll_id = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField(max_length=254)
    
    sem = models.IntegerField()
    cource = models.CharField(max_length=254)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    GENDER_CHOICE = (
    ('other','OTHER'),
    ('male', 'MALE'),
    ('female','female'),
   )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='male')
    cgpa = models.FloatField(max_length=4)
    batch = models.IntegerField() 
    mobile = models.IntegerField()
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name

# class result(models.Model):
#     id = 
