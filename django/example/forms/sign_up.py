from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.password_validation import (
    password_validators_help_text_html,
)
from django.utils.translation import gettext_lazy as _


class SignUpForm(forms.Form):

    username = UsernameField(
        label=_("Username"),
        max_length=150,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
    )

    email = forms.EmailField(label=_("Email address"))

    first_name = forms.CharField(label=_("First name"), max_length=30)

    last_name = forms.CharField(label=_("Last name"), max_length=150)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as before, for verification."),
    )
