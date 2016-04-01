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
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('target_object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='favorites')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'timestamp',
                'ordering': ['-timestamp'],
                'verbose_name': 'favorite',
                'verbose_name_plural': 'favorites',
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'target_content_type', 'target_object_id')]),
        ),
    ]
