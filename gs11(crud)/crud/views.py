from django.shortcuts import redirect, render
from crud.forms import Studentform
from crud.models import StudentRegistration

# Create your views here.
def index(request):
    if request.method == "POST":
        fm = Studentform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = StudentRegistration(name=nm, email=em, password=pw)
            reg.save()
            fm = Studentform()
    else:
        fm = Studentform()
    stud = StudentRegistration.objects.all()
    return render(request, 'crud/add_and_show.html', {'form':fm, 'stu':stud})

def update(request, id):
    if request.method == "POST":
        pi = StudentRegistration.objects.get(pk=id)
        fm = Studentform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = StudentRegistration.objects.get(pk=id)
        fm = Studentform(instance=pi)

    return render(request, 'crud/update.html', {'form':fm})

def delete(request,id):
    if request.method == "POST":
        dlt = StudentRegistration.objects.get(pk=id)
        dlt.delete()
        return redirect('/')