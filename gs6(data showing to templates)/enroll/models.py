from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    roll = models.IntegerField()

    def __str__(self):
        return f'{self.name}\'s id : {self.stuid}'