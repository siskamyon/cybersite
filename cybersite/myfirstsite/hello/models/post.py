from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    date = models.DateTimeField(default=timezone.now)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    author = models.ForeignKey ('Person', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})