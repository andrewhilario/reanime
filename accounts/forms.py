from django import forms
from django.db.models import fields
from .models import *

class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),
    required=True)

    class Meta:
        model = Reviews
        fields = ('text', 'rate')


class AnimeSearchForm(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Anime Review'}), required=False)

    class Meta:
        model = Anime
        fields = ('search',)