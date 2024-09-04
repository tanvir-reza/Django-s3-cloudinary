from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title
