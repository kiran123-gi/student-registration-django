from django import forms
from application.models import StudentModel
class StudentForm(forms.ModelForm):
    class  Meta:
        model = StudentModel
        fields = ['name','age','city','fee']

