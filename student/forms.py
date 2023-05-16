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