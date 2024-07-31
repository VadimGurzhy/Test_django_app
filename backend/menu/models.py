from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'


class Item_menu(models.Model):
    name = models.CharField('Название', max_length=100)
    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Меню',
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
