# Generated by Django 3.0.8 on 2020-12-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, verbose_name='Слаг')),
                ('description', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='complex/', verbose_name='Превью')),
            ],
            options={
                'verbose_name': 'Жилой комплекс',
                'verbose_name_plural': 'Жилые комплексы',
            },
        ),
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение пользователя')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка на продажу квартиры',
                'verbose_name_plural': 'Заявки на продажу квартир',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.IntegerField(verbose_name='Номер дома')),
                ('complex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='service.Complex', verbose_name='Комплекс')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
        migrations.CreateModel(
            name='ComplexGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gal_img', models.ImageField(blank=True, upload_to='complex/gallery/', verbose_name='Фотография')),
                ('complex', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='service.Complex', verbose_name='Название ЖК')),
            ],
            options={
                'verbose_name': 'Фотография ЖК',
                'verbose_name_plural': 'Фотографии ЖК',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_number', models.IntegerField(verbose_name='Номер')),
                ('level', models.IntegerField(verbose_name='Этаж')),
                ('room', models.IntegerField(verbose_name='Кол-во комнат')),
                ('square', models.FloatField(verbose_name='Площадь')),
                ('finishing', models.BooleanField(default=False, verbose_name='Отделка')),
                ('price_m', models.DecimalField(decimal_places=1, max_digits=7, verbose_name='Цена за м2')),
                ('price_total', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Цена за объект')),
                ('plan_img', models.ImageField(upload_to='complex/apartment/', verbose_name='Планировка')),
                ('house', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='service.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
            },
        ),
    ]
