from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import form_view
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from example.forms import SignUpForm


implemented = Package("example.implemented")
functions = Package("example.functions")


@form_view
class SignUpView(Injector):

    template_name = "sign_up.html"
    form_class = SignUpForm

    sign_up = implemented.SignUp.register_user

    data = this.form.cleaned_data

    @operation
    def form_valid(sign_up, data, form, view, request):

        result = sign_up.run(data, request)
        if result.is_success:
            return redirect("/")
        elif result.failed_on("compare_passwords"):
            form.add_error("password2", _("The two password fields didn't match."))
            return view.form_invalid(form)
        elif result.failed_on("validate_password_strength"):
            form.add_error("password1", result.reason)
            return view.form_invalid(form)
