from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Книги')

 
class Product(models.Model):

    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    owner = models.CharField(max_length=20, verbose_name='Автор')
