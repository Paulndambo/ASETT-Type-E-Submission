from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from decimal import Decimal

from cryptoapp.forms import PortfolioForm
from cryptoapp.models import Portfolio, CryptoCurrency, Wallet, Transaction

# Create your views here.
@login_required(login_url="/users/login/")
def wallet(request):
    user = request.user
    currencies = CryptoCurrency.objects.all()
    wallet = Wallet.objects.filter(user=user).first()

    transactions = Transaction.objects.filter(Q(send_from__user=user) | Q(send_to__user=user))

    if not wallet:
        return redirect("new-wallet")

    portfolios = wallet.portfolios.all()
    currencies_in_customer_wallet = CryptoCurrency.objects.filter(
        id__in=list(portfolios.values_list('currency_id', flat=True))
    )

    total_balance = sum(list(portfolios.values_list("coin_total_value", flat=True)))


    context = {
        "wallet": wallet,
        "user": user,
        "currencies": currencies,
        "portfolios": portfolios,
        "total_balance": total_balance,
        "customer_coins": currencies_in_customer_wallet,
        "transactions": transactions
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
    return render(request, "cryptoapp/new_wallet.html")



@login_required(login_url="/users/login/")
def transfer_coins(request):
    if request.method == "POST":
        user = request.user

        wallet_id = request.POST.get("wallet_address")
        amount = Decimal(request.POST.get("amount"))
        currency_id = int(request.POST.get("currency"))

        # Get the two wallets involved in this transaction
        sending_wallet = Wallet.objects.filter(user=user).first()
        receiving_wallet = Wallet.objects.get(wallet_id=wallet_id)

        currency = CryptoCurrency.objects.filter(id=currency_id).first()
        coin_from_portfolio = Portfolio.objects.filter(wallet=sending_wallet, currency=currency).first()
        transacted_amount = amount * currency.current_price
        

        if amount > coin_from_portfolio.amount:
            # Keeping A record of the failed transaction 
            failed_transaction = Transaction.objects.create(
                send_from=sending_wallet,
                send_to=receiving_wallet,
                amount=amount,
                currency=currency,
                status="failed"
            )
            return redirect("failed-transaction")

        else:
            ## Updating Balances on the source wallet
            coin_from_portfolio.amount -= amount
            coin_from_portfolio.coin_total_value -= transacted_amount
            coin_from_portfolio.save()


            # Check if the wallet receiving has this coin listed, if not, list it on their portfolio
            coin_on_receiving_portfolio = Portfolio.objects.filter(wallet=receiving_wallet, currency=currency).first()
            if not coin_on_receiving_portfolio:
                Portfolio.objects.create(
                    wallet=receiving_wallet,
                    currency=currency,
                    amount=amount,
                    coin_total_value=transacted_amount
                )
            else:
                ## Updating Balances on the receiving wallet
                coin_on_receiving_portfolio.amount += amount
                coin_on_receiving_portfolio.coin_total_value += transacted_amount
                coin_on_receiving_portfolio.save()


            # Keeping A record of the successful transaction 
            success_transaction = Transaction.objects.create(
                send_from=sending_wallet,
                send_to=receiving_wallet,
                amount=amount,
                currency=currency,
                status="successful"
            )
            return redirect("wallet")

    return render(request, "modals/transfer_coins.html")


@login_required(login_url="/users/login/")
def failed_wallet_transaction(request):
    return render(request, "transactions/failed_transaction.html")


@login_required(login_url="/users/login/")
def add_coins_to_wallet(request):
    if request.method == "POST":
        currency_id = request.POST.get("currency")
        username = request.POST.get("user")
        amount = request.POST.get("amount")

        user = request.user
        
        wallet = Wallet.objects.filter(user=user).first()
        currency = CryptoCurrency.objects.filter(id=int(currency_id)).first()

        coins_total_value = currency.current_price * Decimal(amount)

        if wallet:
            
            coin_exists = Portfolio.objects.filter(currency=currency, wallet=wallet).first()

            if coin_exists:
                coin_exists.amount += Decimal(amount)
                coin_exists.coin_total_value += coins_total_value
                coin_exists.save()
                print("Coin Exists in Wallet!")
            
            else:
                Portfolio.objects.create(
                    wallet=wallet,
                    currency=currency,
                    amount=float(amount),
                    coin_total_value=coins_total_value
                )
            return redirect("wallet")
            
        
        print(type(currency_id), amount)

    
    return render(request, "modals/create_coins.html")