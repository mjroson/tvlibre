from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _

from embed_video.fields import EmbedVideoField

from taggit.managers import TaggableManager

from apps.favorite.models import Favorite
from apps.notification.models import Notification

from django_extensions.db.models import TimeStampedModel

from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField,
)
from django.contrib.auth import get_user_model


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]


class Program(TimeStampedModel):
    user = models.ForeignKey(User, related_name='programs')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='program')
    category = models.ForeignKey(Category, related_name='programs')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '#%s/' % self.slug

    class Meta:
        verbose_name = _("Program")
        verbose_name_plural = _("Programs")
        ordering = ["title"]


class Episode(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    video = EmbedVideoField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='episode')
    short_description = models.CharField(max_length=150)
    program = models.ForeignKey(Program, related_name='episodes')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '?watch=%s#%s' %(self.slug, self.program.slug)

    class Meta:
        verbose_name = _("Episode")
        verbose_name_plural = _("Episodes")
        ordering = ["-pub_date"]



@receiver(post_save, sender=Episode)
def episode_post_save(sender, *args, **kwargs):
    episode = kwargs['instance']
    if kwargs['created']:
        for tag in episode.short_description.split(' '):
            episode.tags.add(tag)

        try:
            favorites = Favorite.objects.for_object(episode.program, Program)
            for favorite in favorites:
                notification = Notification()
                notification.message = _("Hay episodios nuevos del programa %s" % favorite.target.title)
                notification.user = favorite.user
                notification.obj = episode
                notification.save()
        except:
            pass