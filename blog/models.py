from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    blog_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


