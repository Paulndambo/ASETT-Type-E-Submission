from django import forms

from cryptoapp.models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["currency", "wallet", "amount"]

        widgets = {
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'wallet': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }