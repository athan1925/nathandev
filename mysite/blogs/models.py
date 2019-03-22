from django.db import models

from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', blank=True)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '     .....'

