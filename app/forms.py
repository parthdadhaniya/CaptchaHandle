

from app.models import Student
from django import forms
from captcha.fields import CaptchaField


class StudentForm(forms.ModelForm):
    captcha = CaptchaField()
    
    
    class Meta:
        model = Student
        fields = ("name", "email", "captcha")