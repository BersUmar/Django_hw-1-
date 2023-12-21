# Generated by Django 4.2.7 on 2023-11-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('purchase_price', models.FloatField(verbose_name='цена за покупку')),
                ('date_of_creation', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateField(auto_now=True, verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
    ]