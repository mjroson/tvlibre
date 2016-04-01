from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch.dispatcher import receiver

from allauth.account.signals import user_signed_up


@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def user_signed_up_(request, user, **kwargs):
    if user.is_staff and user.email:
        html_content = "Hola %s; \n Te has registrado a [PROJECT] como usuario avanzado, para poder acceder " \
                       "al panel donde se puede administrar los programas y episodios debes ingresar http://localhost/administrador/"

        msg = EmailMultiAlternatives('PROJECT - Notifications',
                                          html_content,
                                          user.email,
                                          [settings.DEFAULT_FROM_EMAIL])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

