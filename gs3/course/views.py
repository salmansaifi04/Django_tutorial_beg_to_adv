from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse("This is a learn django view")

def learn_python(request):
    return HttpResponse("This is a learn python view")