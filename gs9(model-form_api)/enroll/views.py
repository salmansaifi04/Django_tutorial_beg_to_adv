from django.shortcuts import render
from enroll.forms import UserRegistration
from enroll.models import User


# Create your views here.
def index(request):
    if request.method == "POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    return render(request, 'enroll/index.html', {'form':fm})