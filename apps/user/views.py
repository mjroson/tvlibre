from django.views.generic import CreateView

from .forms import CustomRegisterForm

from allauth.account.views import SignupView


class CustomRegisterView(SignupView):
    form_class = CustomRegisterForm


