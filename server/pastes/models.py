from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Paste(models.Model):  
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(default = '')
    language = models.CharField(max_length = 255, default = 'Java')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detail')

class Language(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail')
