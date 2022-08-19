from django.shortcuts import render
from school.models import Contractor, Student, Teacher, ExamCenter, MyExamCenter

# Create your views here.
def home(request):
    c = Contractor.objects.all()
    s = Student.objects.all()
    t = Teacher.objects.all()
    ExamC = ExamCenter.objects.all()
    MyExamC = MyExamCenter.objects.all()
    return render(request, 'school/home.html', {'con' : c, 'students' : s, 'teachers' : t, 'exam_centers' : ExamC, 'my_exam_centers' : MyExamC})