from django import forms

import itertools
from django.utils.text import slugify

from django.utils.translation import ugettext_lazy as _

from .models import Episode, Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = (
            'title',
            'description',
            'image',
            'category'
        )
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'image': _('Image'),
        }
        help_texts = {
            'description': _('The description is to apear on the list all episode.'),
        }
        error_messages = {
            'title': {
                'max_length': _("This program's title is too long."),
            },
        }


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = (
            'title',
            'short_description',
            'program',
            'description',
            'pub_date',
            'image',
            'video'
        )
        widgets = {
            'description': forms.Textarea(attrs={'class': 'rich_text'}),
        }
        labels = {
            'title': _('Title'),
            'short_description': _('Short Description'),
            'description': _('Description'),
            'pub_date': _('Publication Date'),
            'image': _('Image'),
        }
        help_texts = {
            'short_description': _('The short description is to apear on the list all episode.'),
        }
        error_messages = {
            'title': {
                'max_length': _("This episode's title is too long."),
            },
        }

    def save(self, *args, **kwargs):
        if self.instance.pk:
            return super(EpisodeForm, self).save()

        instance = super(EpisodeForm, self).save(commit=False)

        max_length = Episode._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Episode.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)

        instance.save()

        return instance