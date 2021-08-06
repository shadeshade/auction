from django.forms import ModelForm
from django import forms
from .models import BiddingItem


class BiddingItemCreateViewForm(ModelForm):

    class Meta:
        model = BiddingItem

        fields = [
            'item_name',
            'image',
            'description',
            'price',
            'auction_starts_at',
            'auction_ends_at',
        ]


class BiddingItemForm(forms.Form):
    bid = forms.IntegerField()
