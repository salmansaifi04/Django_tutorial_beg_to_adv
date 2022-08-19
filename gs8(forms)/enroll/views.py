from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.http import HttpResponseRedirect
from enroll.models import User

# Create your views here.
def thankyou(request):
    return render(request, 'enroll/success.html')

def index(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            # print("Form validation")
            # print('Name : ', nm)
            # print('Email : ', em)
            # print('Password : ', ps)
            ## save data to database
            u = User(name = nm, email = em, password = ps) 
            u.save()
            ## update
            # u = User(id=1,name = nm, email = em, password = ps) 
            # u.save()
            ## delete 
            # u = User(id=1) 
            # u.delete()          
            return HttpResponseRedirect('/enroll/success/')
            # return render(request, 'enroll/success.html', {'nm':nm, 'em': em, 'ps' : ps})
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/index.html', {'form':fm})