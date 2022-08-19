from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studetail(request):
    stu = Student.objects.all()
    return render(request, 'enroll/studetails.html', {'stu':stu})