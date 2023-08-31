from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cryptoapp.load_coins_to_db import get_coins_to_update
# Create your views here.

@login_required(login_url="/users/login/")
def home(request):
    print("Coins prices updated on the db")
    get_coins_to_update()
    return render(request, "home.html")