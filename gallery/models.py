from django.db import models
from django.shortcuts import reverse
from datetime import date
from landing.models import SEOOptimizable


class Album(SEOOptimizable):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/albums/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст')
    date = models.DateField(default=date.today, verbose_name='Дата создания')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    def get_absolute_url(self):
        return reverse('album', args=[self.slug])
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return '%s' % self.title


class ImageInAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/albums/%s/%s' % (self.album.id, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '%s' % self.id