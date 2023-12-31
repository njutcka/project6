# Generated by Django 4.2.7 on 2023-12-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='превью')),
                ('date_of_creation', models.DateTimeField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блоговая запись',
                'verbose_name_plural': 'блоговые записи',
            },
        ),
    ]
