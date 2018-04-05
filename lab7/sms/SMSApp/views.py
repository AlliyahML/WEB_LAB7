from django.shortcuts import render
#from folder import className
from .students import Student
from .courses import Courses
from .students import StudentForm

# Create your views here.
def full_student_listing(request):
    allStudents = Student.objects.all()
    allCourses = Courses.objects.all()
    print(allStudents)
    #students in template folder
    return render(request,'students/index.html',{'xx':allStudents,'yy':allCourses})

def add_student(request):
    form =StudentForm()
    return render(request,'students/add.html',{'form':form})
    
