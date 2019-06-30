from django.db import models


class Note(models.Model):
    BOY = 'boy'
    GIRL = 'girl'
    SEX_CHOICE = [
        (BOY, 'Мальчик'),
        (GIRL, 'Девочка'),
    ]

    parent_name = models.CharField(max_length=250, verbose_name='Имя родителя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    child_name = models.CharField(max_length=250, verbose_name='Имя ребенка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=20, choices=SEX_CHOICE, verbose_name='Пол ребенка', default=BOY)
    text = models.TextField(verbose_name='Ожидания от занятий')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return '%s' % self.parent_name