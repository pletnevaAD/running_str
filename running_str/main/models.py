from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class UsersRequest(models.Model):
    text = models.CharField(max_length=200)
    background_color = ColorField(format="hexa")
    text_color = ColorField(format="hexa")
    video_file = models.FileField(upload_to='', null=True)
