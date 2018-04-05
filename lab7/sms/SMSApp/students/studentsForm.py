from django.forms import ModelForm
from .student import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude=()