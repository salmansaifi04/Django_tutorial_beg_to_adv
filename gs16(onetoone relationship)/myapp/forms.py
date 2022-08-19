from django import forms
from myapp.models import Like
from datetime import date

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        widgets ={
            'page_publish_date' : forms.DateInput(),
        }
        fields = "__all__"
        