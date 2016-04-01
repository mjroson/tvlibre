# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
import django_extensions.db.fields
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from='name', unique=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField()),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(upload_to='episode')),
                ('short_description', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'Episode',
                'verbose_name_plural': 'Episodes',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='program')),
                ('category', models.ForeignKey(to='program.Category', related_name='programs')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='programs')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='program',
            field=models.ForeignKey(to='program.Program', related_name='episodes'),
        ),
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
