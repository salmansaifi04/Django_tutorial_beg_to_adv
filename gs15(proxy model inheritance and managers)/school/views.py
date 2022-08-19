from django.shortcuts import render
from .models import ExamCenter, MyExamCenter, Student
# Create your views here.


def proxy(request):
    ec = ExamCenter.Exam.all()
    mec = MyExamCenter.Exam.all()
    custom = MyExamCenter.stud.all()
    # ec = ExamCenter.objects.all()
    # mec = MyExamCenter.objects.all()
    return render(request, 'school/proxy.html', {'exam_centers':ec, 'my_exam_centers':mec, 'custom_centers':custom})

## home
def home(request):
    stu = Student.objects.all()
    stu1 = Student.students.all()
    stu2 = Student.students.get_stu_roll_range(101, 106)
    return render(request, 'school/home.html', {'students':stu, 'stu_manager':stu1, 'stu_roll':stu2})