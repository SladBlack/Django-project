# Generated by Django 3.0.8 on 2020-12-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_apartment_num_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='num_house',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер квартиры по счёту в этом комплексе'),
        ),
    ]
