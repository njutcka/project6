# Generated by Django 4.2.7 on 2023-12-03 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]