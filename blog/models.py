from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Highlight(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self): #new
        self.save()

    def __str__(self):
        return self.title


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title