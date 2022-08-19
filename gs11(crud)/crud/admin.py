from django.contrib import admin
from crud.models import StudentRegistration
# Register your models here.

@admin.register(StudentRegistration)
class AdminStudent(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')



# salman
# salman@123