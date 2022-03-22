from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """ Overwritten Django's original registration form. It adds a field for email """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
