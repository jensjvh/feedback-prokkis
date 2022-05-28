from django.db import models
from django.contrib.auth.models import user

class currentUser(models.Model):
    image = models.ImageField(upload_to = 'user-images')
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)

class productRequests(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    upvotes = models.IntegerField()
    status = models.CharField(max_length = 100)