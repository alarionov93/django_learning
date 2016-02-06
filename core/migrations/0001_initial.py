# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'Authors',
                'verbose_name': '\u0410\u0432\u0442\u043e\u0440',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateField(default=b'2016-02-02')),
                ('author', models.ForeignKey(to='core.Author', db_column=b'author_id')),
            ],
            options={
                'db_table': 'Books',
                'verbose_name': '\u041a\u043d\u0438\u0433\u0430',
                'verbose_name_plural': '\u041a\u043d\u0438\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Categories',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('categories', models.ManyToManyField(to='core.Category')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Farmers',
                'verbose_name': '\u0424\u0435\u0440\u043c\u0435\u0440',
                'verbose_name_plural': '\u0424\u0435\u0440\u043c\u0435\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(to='core.Category')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'Products',
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='farmer',
            name='products',
            field=models.ManyToManyField(to='core.Product'),
        ),
    ]
