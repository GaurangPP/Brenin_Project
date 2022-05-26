from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.TextField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    number = models.IntegerField(default=0)
    query = models.TextField(max_length=500)
    voice = models.FileField()
