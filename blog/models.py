from django.db import models

class Post(models.Model):
    userid = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    slug = models.SlugField(max_length=200, unique=True)