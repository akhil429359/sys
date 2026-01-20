from django.db import models

# Create your models here.

class Student(models.Model):
    STATUS_CHOICES = [
        ('active','Active'),
        ('inactive','Inactive'),
        ('graduated','Graduated')

    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='active')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
