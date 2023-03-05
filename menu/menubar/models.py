from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=20)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField('Текст', max_length=30)
    url = models.CharField('URL при переходе', max_length=30, default='/')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Вложен в',
                               null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
