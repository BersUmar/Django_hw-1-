from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.FloatField(verbose_name='цена за покупку', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.DateField(verbose_name='дата последнего изменения', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.description} {self.purchase_price} '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @property
    def active_version(self):
        return self.version_set.get(version_flag=True)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    num_version = models.IntegerField(verbose_name='Номер версии', **NULLABLE)
    name_version = models.CharField(max_length=150, verbose_name='Название версии', **NULLABLE)
    version_flag = models.BooleanField(default=False, verbose_name='Прикнак активности')

    def __str__(self):
        return f'{self.name_version} {self.product} {self.num_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'