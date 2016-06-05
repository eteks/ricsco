# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ricsco.util


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='confirmation_key',
            field=models.CharField(default=ricsco.util.make_uuid, help_text=b'Registered user validate email', max_length=128),
        ),
    ]
