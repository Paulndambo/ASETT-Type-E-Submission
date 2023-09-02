from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cryptoapp.load_coins_to_db import get_coins_to_update
from cryptoapp.models import CryptoCurrency
# Create your views here.

#@login_required(login_url="/users/login/")
def home(request):
    print("Coins prices updated on the db")
    currencies = CryptoCurrency.objects.all()
    if request.method == "POST":
        currency = request.POST.get("currency")
        currencies = CryptoCurrency.objects.filter(name__icontains=currency)

    context = {
        "currencies": currencies
    }
    return render(request, "home.html", context)