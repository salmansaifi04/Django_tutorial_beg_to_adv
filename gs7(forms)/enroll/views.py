from django.shortcuts import render
from enroll.forms import StudentRegistration
# Create your views here.
def index(request):
    fm = StudentRegistration()
    return render(request, 'enroll/index.html', {'form':fm})