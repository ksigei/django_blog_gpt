from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
