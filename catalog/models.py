from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = None
    category = models.CharField(max_length=100, verbose_name='категория')
    description_category = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='название')
    description_product = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', null=True)
    price = models.FloatField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(verbose_name='дата создания', default=None, **NULLABLE)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', default=None, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.IntegerField(verbose_name='номер_версии')
    name = models.CharField(max_length=100, verbose_name='название версии')
    current_version = models.BooleanField(default=True, verbose_name='признак_текущей_версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'