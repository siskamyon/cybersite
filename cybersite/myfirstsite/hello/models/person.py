from django.db import models

# Create your models here.
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    

