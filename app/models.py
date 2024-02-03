from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Student Name")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Student email")
    
    def __str__(self):
        return str(self.name)