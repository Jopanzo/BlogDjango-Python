from django.db import models

# Create your models here.
class User(models.Model):
    firstName  = models.CharField(max_length = 30)
    lastName   = models.CharField(max_length = 30)
    email      = models.EmailField(max_length = 30, unique = True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)