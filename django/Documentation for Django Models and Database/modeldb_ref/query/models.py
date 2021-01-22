from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = [
        ('S', 'Short'),  # first value stored in the database
        ('M', 'Medium'),  # second value displayed in the form widget
        ('L', 'Large'),
    ]
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    age = models.CharField(max_length=30, primary_key=True)
