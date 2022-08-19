from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(max_length=70, error_messages={'required':'Enter your name'})
    email = forms.EmailField(max_length=70, error_messages={'required':'Enter your email'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required':'Enter your password'})