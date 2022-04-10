from django.db import models
from django.urls import reverse

class Posts(models.Model):
    author = models.CharField('Author', max_length=30)
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Publish date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.author}/list'

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
