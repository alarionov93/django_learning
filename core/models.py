# -*- coding=utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.ForeignKey("Author", to_field="id", db_column="author_id")
    date = models.DateField(null=False, default=timezone.now().strftime("%Y-%m-%d"))

    def __unicode__(self):
        return "%s, %s" % (self.title, self.author.full_name)

    class Meta:
        db_table = "Books"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    second_name = models.CharField(max_length=50, unique=False, null=True, blank=False)
    first_name = models.CharField(max_length=50, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=50, unique=False, null=True, blank=True)

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        n = "%s %s %s" % (self.second_name, self.first_name, self.last_name)
        return n.strip()

    class Meta:
        db_table = "Authors"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=False, null=False, blank=False)

    def __unicode__(self):
        return self.category_name

    class Meta:
        db_table = "Categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model): #TODO: many products to one category!
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.product_name

    class Meta:
        db_table = "Products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ('id', )


class Farmer(models.Model): #TODO: on farmer adding get categories by selected products, it is not convinient to remember category of each product!!!
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    last_name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    email = models.EmailField(blank=False, null=False, unique=True) #TODO: extend django user model here!
    products = models.ManyToManyField(Product)
    categories = models.ManyToManyField(Category)

    @property
    def full_name(self):
        str = "%s %s" % (self.first_name, self.last_name)
        return str.strip()

    def __unicode__(self):
        return self.full_name

    class Meta:
        db_table = "Farmers"
        verbose_name = "Фермер"
        verbose_name_plural = "Фермеры"
        ordering = ('id', )

