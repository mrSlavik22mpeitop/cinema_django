from django.db import models


class News(models.Model):
    image_news = models.ImageField(upload_to='news/')
    date_news = models.DateField(max_length=70)
    title_news = models.CharField(max_length=70)
    description_news = models.CharField(max_length=1000)

    def __str__(self):
        return self.title_news

    class Meta:
        ordering = ['id']
# Create your models here.
