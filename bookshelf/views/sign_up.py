from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from bookshelf.forms import SignUpForm
from bookshelf.implemented import SignUp


class SignUpView(FormView):
    template_name = "sign_up.html"
    form_class = SignUpForm

    def form_valid(self, form):
        result = SignUp.register_user.run(data=form.cleaned_data, request=self.request)
        if result.is_success:
            return redirect("/")
        elif result.failed_on("compare_passwords"):
            form.add_error("password2", _("The two password fields didn't match."))
            return self.form_invalid(form)
        elif result.failed_on("validate_password_strength"):
            form.add_error("password1", result.reason)
            return self.form_invalid(form)
