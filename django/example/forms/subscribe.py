from django import forms


class SubscribeForm(forms.Form):

    price_id = forms.CharField(widget=forms.HiddenInput())
