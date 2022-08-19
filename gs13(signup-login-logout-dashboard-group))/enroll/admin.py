from django.contrib import admin
from enroll.models import Blog

# Register your models here.
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']




## super user
#admin 
#admin@123

## user
# salman
# saifi@123 