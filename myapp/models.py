from django.db import models
from django.contrib.auth.models import User

class Yunalishlar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/imgs/yunalishlar/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='static/imgs/teachers/', blank=True, null=True)
    def __str__(self):
        return self.full_name


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='static/imgs/news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Reception(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='static/files/reception/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    passport = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    yunalish = models.ForeignKey('Yunalishlar', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name