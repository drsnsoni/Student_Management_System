from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Activity, Assignment


#register Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email','password1', 'password2']

#Student Form
class StudentForm(forms.ModelForm):
    name  = forms.TextInput()
    email = forms.EmailInput
    Enroll_no = forms.IntegerField()
    date_of_birth = forms.DateInput()
    SPI = forms.IntegerField()
    CGPA = forms.IntegerField()
    sem = forms.IntegerField()
    CHOICE_GENDER = ( ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'Other'),)

    gender = forms.ChoiceField(choices = CHOICE_GENDER)
    mobile_no = forms.IntegerField()
    parents_no = forms.IntegerField()
    address =forms.TextInput()
    class Meta:
        model = Student
        fields = (
            'name',
            'profile_photo',
            'email',
            'Enroll_no',
            'date_of_birth',
            'SPI',
            'CGPA',
            'sem',
            'gender',
            'mobile_no',
            'parents_no',
            'address'
        )

#Activity Form
class activityform(forms.ModelForm):
     activity_title = forms.CharField()
     activity_file = forms.ImageField()
     enroll_no = forms.IntegerField()
     class Meta:
        model = Activity
        fields = (
            'activity_title',
            'activity_file',
            'enroll_no',
        )

#Assignment Form
class assignmentform(forms.ModelForm):
     assignment_title = forms.CharField()
     assignment_file = forms.ImageField()
     enroll_no = forms.IntegerField()
     class Meta:
        model = Assignment
        fields = (
            'assignment_title',
            'assignment_file',
            'enroll_no',
        )