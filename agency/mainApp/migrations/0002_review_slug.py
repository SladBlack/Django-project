# Generated by Django 3.0.8 on 2020-12-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='flatberry', verbose_name='Слаг/Slug'),
        ),
    ]