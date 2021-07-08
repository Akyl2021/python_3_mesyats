from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=100)
    price = models.IntegerField('Цена')
    MFD = models.DateField('Срок годности', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    text = models.CharField('Текст', max_length=100)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='date', null=True)

    def __str__(self):
        return self.text
