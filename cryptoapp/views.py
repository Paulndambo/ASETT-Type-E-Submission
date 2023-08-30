from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cryptoapp.forms import PortfolioForm
from cryptoapp.models import Portfolio, CryptoCurrency, Wallet

# Create your views here.
@login_required(login_url="/users/login/")
def wallet(request):
    user = request.user
    currencies = list(CryptoCurrency.objects.values_list('name', flat=True))
    wallet = Wallet.objects.filter(user=user).first()

    portfolios = wallet.portfolios.all()

    if not wallet:
        return redirect("new-wallet")

    context = {
        "wallet": wallet,
        "user": user,
        "currencies": currencies,
        "portfolios": portfolios
    }
    
    return render(request, "cryptoapp/wallet.html", context)


@login_required(login_url="/users/login/")
def new_wallet(request):
    user = request.user

    if request.method == "POST":
        user_id = request.POST.get("user")
        phone_number = request.POST.get("phone_number")

        wallet = Wallet.objects.create(user=user, phone_number=phone_number)
        return redirect("wallet")

        print(user.id, user_id, phone_number)

    return render(request, "cryptoapp/new_wallet.html")


def add_coins_to_wallet(request):
    if request.method == "POST":
        currency_name = request.POST.get("currency")
        username = request.POST.get("user")
        amount = request.POST.get("amount")

        wallet = Wallet.objects.filter(user__username=username).first()
        currency = CryptoCurrency.objects.filter(name=currency_name).first()

        
        if wallet:
            Portfolio.objects.create(
                wallet=wallet,
                currency=currency,
                amount=float(amount)
            )
            return redirect("wallet")
        print(currency, wallet.id, amount)

    
    return render(request, "modals/create_coins.html")