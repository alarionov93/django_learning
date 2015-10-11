# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.ForeignKey("Author", to_field="id", db_column="author_id")

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
        verbose_name = "Афтар"
        verbose_name_plural = "Афтары"
