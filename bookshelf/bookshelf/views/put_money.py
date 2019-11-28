from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies import this
from dependencies.contrib.django import form_view
from django.shortcuts import redirect

from bookshelf.forms import PutMoneyForm


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@form_view
class PutMoneyView(Injector):

    template_name = "put_money.html"
    form_class = PutMoneyForm

    put_money_into_account = implemented.PutMoneyIntoAccount.put

    amount = this.form.cleaned_data["amount"]

    @operation
    def form_valid(put_money_into_account, amount, request):

        put_money_into_account(profile_id=request.profile_id, amount=amount)
        return redirect("profile")
