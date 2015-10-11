# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151009_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='second_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
