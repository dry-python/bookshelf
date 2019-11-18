from django import forms


class SubscribeForm(forms.Form):

    price_id = forms.IntegerField(widget=forms.HiddenInput())
