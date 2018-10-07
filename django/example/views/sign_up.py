from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import form_view
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from example.forms import SignUpForm


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@form_view
class SignUpView(Injector):

    template_name = "sign_up.html"
    form_class = SignUpForm

    sign_up = services.SignUp.register_user
    validate_password = functions.validate_password
    create_user = repositories.create_user
    save_password = repositories.save_password
    create_profile = repositories.create_profile
    store_user_in_session = functions.StoreUserInSession.do
    send_notification = functions.SendNotification.do
    messages = functions.Messages
    create_notification = repositories.create_notification

    data = this.form.cleaned_data

    @operation
    def form_valid(sign_up, data, form, view):

        result = sign_up.run(data)
        if result.is_success:
            return redirect("/")
        elif result.failed_on("compare_passwords"):
            form.add_error("password2", _("The two password fields didn't match."))
            return view.form_invalid(form)
        elif result.failed_on("validate_password_strength"):
            form.add_error("password1", result.reason)
            return view.form_invalid(form)
