from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label = 'Your Name ', label_suffix=' ')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    comment = forms.CharField(widget=forms.Textarea())
    male = forms.CharField(widget=forms.CheckboxInput)
    upload_file = forms.FileField()
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'first_class',
    }))

