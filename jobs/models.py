from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    topic = models.CharField(max_length=100)
    summary = models.TextField()
    url = EmbedVideoField(blank=True)

    def __str__(self):
        return self.topic
