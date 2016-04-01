from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from .managers import NotificationManager


class Notification(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'), related_name='notifications')
    content_type = models.ForeignKey(ContentType, related_name='notifications')
    object_id = models.PositiveIntegerField()
    obj = generic.GenericForeignKey('content_type', 'object_id')
    read = models.DateTimeField(null=True, blank=True, default=None)

    objects = NotificationManager()

    def get_url(self):
        if self.obj:
            return self.obj.get_absolute_url()
        else:
            return ''

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ["-created"]


@receiver(post_save, sender=Notification)
def notification_post_save(sender, *args, **kwargs):
    """
        Cada vez que se crea una notificacion y el usuario asociado tiene un email, se lo notifica por ese medio.
    """
    notification = kwargs['instance']
    if kwargs['created']:
        # Send notification
        if notification.user.email:
            context = {}
            context['notification'] = notification
            message = render_to_string('notification/emails/notification.html', context)
            msg = EmailMultiAlternatives(_('Tv Libre - Notifications'),
                                         message,
                                         settings.DEFAULT_FROM_EMAIL,
                                         [notification.user.email])
            msg.attach_alternative(message, 'text/html')
            msg.send()
