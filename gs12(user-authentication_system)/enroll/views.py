from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from enroll.forms import SignUpForm, EditUserProfile, EditAdminProfile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


# Create your views here.
## signup function
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Accout created successfully')
        else:
            fm = SignUpForm()
        return render(request, 'enroll/signup.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

## login function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

## profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfile(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile Updated!!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance = request.user)
                users = User.objects.all()
            else:        
                fm = EditUserProfile(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name':request.user, 'form':fm, 'users':users}) 
    else:
        return HttpResponseRedirect('/login/')

## logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


## change password with the old password
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user= request.user)
        return render(request, 'enroll/pass_change.html', {'form':fm})
    else:
        return HttpResponseRedirect('/signin/')


## change password without the old password
def change_pass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password changed successfully!!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user= request.user)
        return render(request, 'enroll/pass_change1.html', {'form':fm})
    else:
        return HttpResponseRedirect('/signin/')

## user detail 
def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfile(instance=pi)
        return render(request, 'enroll/userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
