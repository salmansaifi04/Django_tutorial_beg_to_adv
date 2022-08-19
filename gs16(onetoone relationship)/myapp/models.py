from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    ## here when we dlt the user, page also dlt but when we dlt page user not dlt
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    ## here when we user create a page, then we are not able to dlt this user
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)

    ## user create a post when its status is 'is_staff' or 'is_superuser', other are not able to create a page
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})

    page_name = models.CharField(max_length=100)
    page_cat = models.CharField(max_length=100)
    page_publish_date = models.DateField()

class Like(Page):
    panna = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()