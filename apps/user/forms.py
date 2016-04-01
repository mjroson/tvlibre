from django import forms

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from allauth.account.utils import send_email_confirmation
from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter
from allauth.utils import email_address_exists

class CustomRegisterForm(SignupForm):
    is_staff = forms.BooleanField(help_text='El usuario avanzado tiene la posibilidad de cargar programas y episodios, '
                                            'para este perfil se necesita confirmacion de email para poder activar la cuenta',
                                  label='Registrar como usuario avanzado', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'is_staff',  'email', 'username')

    def __init__(self, *args, **kwargs):
        kwargs['username_required'] = True
        #kwargs['email_required'] = True
        super(CustomRegisterForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        staff = self.data.get('is_staff', 'off')
        if staff == 'on':
            if not value or value == '':
                raise forms.ValidationError("When is staff, email is required")

        if value and email_address_exists(value):
            self.raise_duplicate_email_error()
        return value


    