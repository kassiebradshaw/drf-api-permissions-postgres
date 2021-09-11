from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=64)
    artist = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    listener = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.artist}'
