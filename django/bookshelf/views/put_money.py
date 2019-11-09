from dependencies import Injector, Package, operation, this
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
    def form_valid(put_money_into_account, user, amount):

        put_money_into_account(user=user, amount=amount)
        return redirect("profile")
