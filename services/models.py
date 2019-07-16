from django.db import models
from django.urls import reverse
from landing.models import SEOOptimizable
from tinymce.models import HTMLField


class Specialist(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    about = models.TextField(verbose_name='О специалисте')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/specialists/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Фото')
    
    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return '%s' % self.name


class Category(SEOOptimizable):
    title1 = models.CharField(max_length=120, verbose_name='Название (первая строка)')
    title2 = models.CharField(max_length=120, verbose_name='Название (вторая строка)', blank=True, null=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    color_prefix = models.CharField(max_length=250, verbose_name='Префикс цвета')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ('title1', 'title2')

    def title(self):
        return '%s %s' % (self.title1, self.title2)

    def __str__(self):
        if self.title2:
            return '%s %s' % (self.title1, self.title2)
        else:
            return '%s' % self.title1


class Service(SEOOptimizable):
    categories = models.ManyToManyField(Category, related_name='services', verbose_name='Категории')
    specialists = models.ManyToManyField(Specialist, related_name='services', verbose_name='Специалисты')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    schedule = models.CharField(max_length=250, verbose_name='График')
    one_lesson_price = models.PositiveIntegerField(verbose_name='Цена одного занятия')
    some_lesson_nmb = models.PositiveIntegerField(verbose_name='Количество занятий')
    some_lesson_price = models.PositiveIntegerField(verbose_name='Цена нескольких занятий')
    text = HTMLField(verbose_name='Текст')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '%s' % self.title


class ImageInService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/services/%s/%s' % (self.service.id, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '%s' % self.id


class Artclass(SEOOptimizable):
    categories = models.ManyToManyField(Category, related_name='artclasses', verbose_name='Категории')
    specialists = models.ManyToManyField(Specialist, related_name='artclasses', verbose_name='Специалисты')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)
    schedule = models.CharField(max_length=250, verbose_name='График')
    one_lesson_price = models.PositiveIntegerField(verbose_name='Цена одного занятия')
    some_lesson_nmb = models.PositiveIntegerField(verbose_name='Количество занятий')
    some_lesson_price = models.PositiveIntegerField(verbose_name='Цена нескольких занятий')
    text = HTMLField(verbose_name='Текст')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    
    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'

    def __str__(self):
        return '%s' % self.title


class ImageInArtclass(models.Model):
    artclass = models.ForeignKey(Artclass, on_delete=models.CASCADE, verbose_name='Категория', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        return 'images/artclasses/%s/%s' % (self.artclass.id, filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '%s' % self.id


class WeekDay(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    short_name = models.CharField(max_length=250, verbose_name='Короткое название')
    slug_name = models.CharField(max_length=250, verbose_name='Slug название')
    
    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return '%s' % self.name


class WeekDayServiceElem(models.Model):
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='service_elems', verbose_name='День недели')
    time = models.CharField(max_length=250, verbose_name='Время')
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='service_elems', verbose_name='Специалист')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_elems', verbose_name='Услуга')

    class Meta:
        verbose_name = 'Услуга в расписании'
        verbose_name_plural = 'Услуги в расписании'

    def __str__(self):
        return '%s' % self.service.title


class WeekDayArtclassElem(models.Model):
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='artclass_elems', verbose_name='День недели')
    time = models.CharField(max_length=250, verbose_name='Время')
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='artclass_elems', verbose_name='Специалист')
    service = models.ForeignKey(Artclass, on_delete=models.CASCADE, related_name='artclass_elems', verbose_name='Кружок')

    class Meta:
        verbose_name = 'Кружок в расписании'
        verbose_name_plural = 'Кружки в расписании'

    def __str__(self):
        return '%s' % self.service.title
