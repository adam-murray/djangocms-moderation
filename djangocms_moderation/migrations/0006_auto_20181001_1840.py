# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-01 17:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangocms_moderation', '0005_auto_20180919_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moderationcollection',
            options={'permissions': (('can_change_author', 'Can change collection author'),)},
        ),
        migrations.AddField(
            model_name='moderationrequest',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='author'),
            preserve_default=False,
        ),
    ]
