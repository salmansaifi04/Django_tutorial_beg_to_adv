from django.urls import path
from . import views

urlpatterns = [
    path('studetails/', views.studetail, name='studetails'),
]
