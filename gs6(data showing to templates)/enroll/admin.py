from django.contrib import admin
from .models import Student

# Register your models here.
# 1. first way 
# admin.site.register(Student)

# 2. second way
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('stuid', 'name', 'email', 'phone', 'roll')

# admin.site.register(Student, StudentAdmin)

# 3. third way
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'name', 'email', 'phone', 'roll')