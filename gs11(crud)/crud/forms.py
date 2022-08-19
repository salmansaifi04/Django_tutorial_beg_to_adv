from django import forms
from crud.models import StudentRegistration


class Studentform(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(render_value=True)
        }