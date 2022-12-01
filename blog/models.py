from django.db import models
from django.utils import timezone


# Create your models here.

# Table
# Check more on data types
class Post (models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    # Order the data by publish date
    # A comma is needed at the end to be recognized as Tuple
    class Meta:
        ordering = ('-publish',)