# Generated by Django 3.0.8 on 2020-12-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20201211_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='article/', verbose_name='Фотография статьи'),
        ),
    ]
