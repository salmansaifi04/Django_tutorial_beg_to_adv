from django import forms
from enroll.models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        widgets ={
            'password' : forms.PasswordInput(),
            'name' : forms.TextInput(
                attrs={
                    'class':'first_class'
                }
            )
        }
        fields = "__all__"
