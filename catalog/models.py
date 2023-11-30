from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    objects = None
    category = models.CharField(max_length=100, verbose_name='категория')
    description_category = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.category} {self.description_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('description_category',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description_product = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, default=None, verbose_name='категория')
    price = models.FloatField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(verbose_name='дата создания', default=None, **NULLABLE)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', default=None, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price_for_one}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('description_product',)

