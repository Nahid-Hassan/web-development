# blog/models.py
from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
