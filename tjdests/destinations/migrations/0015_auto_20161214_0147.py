# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0014_auto_20151219_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='ceeb',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
