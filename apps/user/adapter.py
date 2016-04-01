from allauth.account.adapter import DefaultAccountAdapter

from django.contrib.auth.models import Group


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(CustomAccountAdapter, self).save_user(request, user, form, commit=False)
        data = form.cleaned_data
        user.is_staff = data.get('is_staff', False)
        if user.is_staff:
            user.groups.add(Group.objects.first())
        user.save()
        return user