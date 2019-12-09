from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import form_view
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from bookshelf.forms import SignUpForm


implemented = Package("bookshelf.implemented")


@form_view
class SignUpView(Injector):

    template_name = "sign_up.html"
    form_class = SignUpForm

    sign_up = implemented.SignUp.register_user

    @operation
    def form_valid(sign_up, form, view, request):

        result = sign_up.run(data=form.cleaned_data, request=request)
        if result.is_success:
            return redirect("/")
        elif result.failed_on("compare_passwords"):
            form.add_error("password2", _("The two password fields didn't match."))
            return view.form_invalid(form)
        elif result.failed_on("validate_password_strength"):
            form.add_error("password1", result.reason)
            return view.form_invalid(form)
