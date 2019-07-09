from django.db import models
from tinymce.models import HTMLField


class SEOOptimizable(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title')
    desc = models.CharField(max_length=250, verbose_name='Description')
    keywords = models.CharField(max_length=250, verbose_name='Keywords')

    class Meta:
        abstract = True


class TitleTag(SEOOptimizable):
    url = models.CharField(max_length=250, verbose_name='URL')

    class Meta:
        verbose_name = 'SEO title'
        verbose_name_plural = 'SEO titles'

    def __str__(self):
        return '%s' % self.seo_title
    

class MailToString(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Кому отправлять письмо'
        verbose_name_plural = 'Кому отправлять письмо'

    def __str__(self):
        return '%s' % self.email


class MailFromString(models.Model):
    use_tls = models.BooleanField(verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)')
    use_ssl = models.BooleanField(verbose_name='EMAIL_USE_SSL(yandex.ru)')
    port = models.PositiveIntegerField(verbose_name='EMAIL_PORT')
    host = models.CharField(max_length=250, verbose_name='EMAIL_HOST')
    host_user = models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER')
    host_password = models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD')

    class Meta:
        verbose_name = 'Откуда отправлять письмо'
        verbose_name_plural = 'Откуда отправлять письмо'

    def __str__(self):
        return '%s' % self.host_user


class Agreement(SEOOptimizable):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Cоглашение на обработку персональных данных'
        verbose_name_plural = 'Cоглашение на обработку персональных данных'
    
    def __str__(self):
        return self.title


class OurPros(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.CharField(max_length=250, verbose_name='Текст')

    def get_picture_url(self, filename):
        return 'images/our_pros/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Наш плюс'
        verbose_name_plural = 'Наши плюсы'

    def __str__(self):
        return '%s' % self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Текст')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return '%s' % self.title