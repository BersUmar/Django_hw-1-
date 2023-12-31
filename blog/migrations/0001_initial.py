# Generated by Django 4.2.7 on 2023-12-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogWriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('date_of_creation', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Записи блога',
            },
        ),
    ]
