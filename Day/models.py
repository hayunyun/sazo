from django.db import models
from django import forms

class Trip(models.Model):
    objects = models.Manager()
    region = models.CharField(blank=True, max_length=200)
    name =  models.CharField(max_length=500)
    description = models.TextField()
    address = models.TextField()
    price = models.TextField(blank=True)
    time = models.CharField(max_length=500)
    photo = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True)
    theme = models.CharField(blank=True, max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name