# Generated by Django 3.0.8 on 2020-12-11 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20201211_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='agency',
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
    ]
