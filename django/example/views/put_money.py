from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import form_view
from django.shortcuts import redirect

from example.forms import PutMoneyForm


services = Package("example.services")
repositories = Package("example.repositories")


@form_view
class PutMoney(Injector):

    template_name = "put_money.html"
    form_class = PutMoneyForm

    put_money_into_account = services.PutMoneyIntoAccount.put
    load_profile = repositories.load_profile
    add_balance = repositories.add_balance
    save_profile = repositories.save_profile

    amount = this.form.cleaned_data["amount"]

    @operation
    def form_valid(put_money_into_account, user, amount):

        put_money_into_account(user, amount)
        return redirect("profile")
