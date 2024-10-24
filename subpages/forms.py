# forms.py

from django import forms
from .models import Subpage
from casinos.models import Casino

class SubpageCasinoForm(forms.ModelForm):
    casino = forms.ModelChoiceField(queryset=Casino.objects.all(), label='Select Casino')
    affiliate_link = forms.URLField(label='Affiliate Link')

    class Meta:
        model = Subpage
        fields = ['casino', 'affiliate_link']
