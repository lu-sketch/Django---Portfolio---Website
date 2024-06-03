from django.db import models

# Create your models here.
# models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
