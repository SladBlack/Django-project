# Generated by Django 3.0.8 on 2020-12-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='reviews', verbose_name='Слаг/Slug'),
        ),
    ]
