# Generated by Django 4.2.7 on 2023-12-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_user_email_verified_user_ver_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='001579328482', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
