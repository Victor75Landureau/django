# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='./media/image/'),
        ),
    ]
