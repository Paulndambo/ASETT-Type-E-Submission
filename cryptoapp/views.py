from django.shortcuts import render

from cryptoapp.forms import PortfolioForm
from cryptoapp.models import Portfolio, CryptoCurrency, Wallet

# Create your views here.
def wallet(request):
    user = request.user

    

    return render(request, "cryptoapp/wallet.html")



def add_coins_to_wallet(request):
    currencies = list(CryptoCurrency.objects.values_list('name', flat=True))

    if request.method == "POST":
        currency = request.POST.get("currency")
        wallet = request.POST.get("wallet")
        amount = request.POST.get("amount")


    context = {
        "currencies": currencies
    }
    return render(request, "cryptoapp/add_coins.html", context)