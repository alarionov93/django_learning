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
                ('author', models.ForeignKey(to='core.Author', db_column=b'author_id')),
            ],
            options={
                'db_table': 'Books',
                'verbose_name': '\u041a\u043d\u0438\u0433\u0430',
                'verbose_name_plural': '\u041a\u043d\u0438\u0433\u0438',
            },
        ),
    ]
