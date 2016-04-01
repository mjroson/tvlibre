# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('message', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('read', models.DateTimeField(null=True, default=None, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='notifications')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='notifications')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
