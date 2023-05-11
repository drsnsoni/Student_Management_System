from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email','password1', 'password2']

class StudentForm(forms.ModelForm):
    name  = forms.TextInput()
    email = forms.EmailField()
    Enroll_no = forms.IntegerField()
    date_of_birth = forms.DateField()
    SPI = forms.IntegerField()
    CGPA = forms.IntegerField()
    adhar_no = forms.IntegerField()
    sem = forms.IntegerField()
    CHOICE_GENDER = ( ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'Other'),)

    gender = forms.ChoiceField(choices = CHOICE_GENDER)
    mobile_no = forms.IntegerField()
    parents_no = forms.IntegerField()
    parents_email = forms.EmailField()
    address =forms.TextInput()
    class Meta:
        model = Student
        fields = (
            'name',
            'email',
            'Enroll_no',
            'date_of_birth',
            'SPI',
            'CGPA',
            'adhar_no',
            'sem',
            'gender',
            'mobile_no',
            'parents_no',
            'parents_email',
            'address'
        )