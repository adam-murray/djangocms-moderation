# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-02 16:25
from __future__ import unicode_literals

from django.db import migrations


def moderationrequest_author(apps, schema_editor):
    ModerationRequest = apps.get_model('djangocms_moderation', 'ModerationRequest')
    for mr in ModerationRequest.objects.all():
        mr.author = mr.collection.author
        mr.save()


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_moderation', '0006_auto_20181001_1840'),
    ]

    operations = [
        migrations.RunPython(moderationrequest_author),
    ]
