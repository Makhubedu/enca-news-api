from django.db import models

# Create your models here.
class News(models.Model):
    them_images = models.URLField()
    body_title = models.CharField(max_length=200)
    summary = models.CharField(max_length=30000)
    links = models.CharField(max_length=4000)

class MainNews(models.Model):
    title = models.CharField(max_length=200)
    lead_content = models.CharField(max_length=30000)
    image_caption = models.CharField(max_length=30000, default="")
    img = models.CharField(max_length=4000)