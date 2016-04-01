# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import get_model


def _get_content_type_and_obj(obj, model=None):
    if isinstance(model, str):
        model = get_model(*model.split("."))

    if isinstance(obj, (int,)):
        obj = model.objects.get(pk=obj)

    return ContentType.objects.get_for_model(type(obj)), obj


class NotificationManager(models.Manager):
    """
    A Manager for Notification objects
    """

    def for_user(self, user, model=None):
        """
        Returns a Notification objects queryset for a given user.

        If a model params is provided, it returns only the
        notification objects of that model class

        Usage:

            Notification.objects.for_user(user)
            Notification.objects.for_user(user, model=Program)
            Notification.objects.for_user(user, model="program.Program")
        """

        qs = self.get_queryset().filter(user=user)

        if model:
            if isinstance(model, str):
                model = get_model(*model.split("."))

            content_type = ContentType.objects.get_for_model(model)
            qs = qs.filter(target_content_type=content_type)

        return qs.order_by("-created")

    def for_model(self, model):
        """
        Returns a Notification objects queryset for a given model.
        `model` may be a django model class or an string representing
        a model in module-notation, ie: "auth.User"

        Usage:

            Notification.objects.for_model(Program)
            Notification.objects.for_model("program.Program")
        """

        # if model is an app_label.model string make it a Model class
        if isinstance(model, str):
            model = get_model(*model.split("."))

        content_type = ContentType.objects.get_for_model(model)

        qs = self.get_queryset().filter(
            target_content_type=content_type
        )

        return qs.order_by("-created")

    def for_object(self, obj, model=None):
        """
        Returns a Notification objects queryset for a given object

        Usage:
            Notification.objects.for_object(1, "program.Program")
            Notification.objects.for_object(1, Program)

        or given a music app with a Program model:

            program = Program.objects.get(pk=1)
            Notification.objects.for_object(program)
        """

        content_type, obj = _get_content_type_and_obj(obj, model)

        qs = self.get_queryset().filter(
            target_content_type=content_type,
            target_object_id=obj.pk
        )

        return qs.order_by("-created")

    def get_notification(self, user, obj, model=None):
        """
        Returns a Notification instance if the `user` has notification
        the given object `obj`. Otherwise returns None

        Usage:
            Notification.objects.get_notification(user, 1, "rp.Event")
            Notification.objects.get_notification(user, 1, Event)

        or given a music app with a Program model:

            program = Program.objects.get(pk=1)
            Notification.objects.get_notification(user, program)
        """

        content_type, obj = _get_content_type_and_obj(obj, model)

        try:
            return self.get_queryset().get(
                user=user,
                target_content_type=content_type,
                target_object_id=obj.id
            )
        except self.model.DoesNotExist:
            return None


