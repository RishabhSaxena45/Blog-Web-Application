from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()
    