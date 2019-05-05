from django.db import models
from django import forms

class Trip(models.Model):
    objects = models.Manager()
    r
    name =  models.CharField(max_length=500)
    description = models.TextField()
    address = models.TextField()
    price = models.IntegerField()
    time = models.CharField(max_length=500)
    photo = models.ImageField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

