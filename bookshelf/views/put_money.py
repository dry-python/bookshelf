from django.shortcuts import redirect
from django.views.generic import FormView

from bookshelf.forms import PutMoneyForm
from bookshelf.implemented import PutMoneyIntoAccount


class PutMoneyView(FormView):
    template_name = "put_money.html"
    form_class = PutMoneyForm

    def form_valid(self, form):
        PutMoneyIntoAccount.put(
            profile_id=self.request.profile_id, amount=form.cleaned_data["amount"]
        )
        return redirect("profile")
