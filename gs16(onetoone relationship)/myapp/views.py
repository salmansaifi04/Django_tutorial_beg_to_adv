from django.shortcuts import render
from .models import Page, User
from .forms import LikeForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    pages = Page.objects.all()
    users = User.objects.all()
    return render(request, 'myapp/home.html', {'pages':pages, 'users':users})

def user_likes(request):
    if request.method == "POST":
        fm = LikeForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully created!!!')
            return HttpResponseRedirect('/home/')
        else:
            messages.error(request, 'Plz select the another user')
            return HttpResponseRedirect('/')
    else:
        fm = LikeForm()
    return render(request, 'myapp/likes.html', {'form':fm})
