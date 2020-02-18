from django.db import models
# Create your models here.
class Blog(models.Model):
    blogTitle = models.CharField(max_length = 120)
    blogContent = models.TextField()
    blogAuthor = models.CharField(max_length = 120)