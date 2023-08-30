from django.urls import path
from cryptoapp.views import add_coins_to_wallet, new_wallet, wallet


urlpatterns = [
    path("record-coins/", add_coins_to_wallet, name="record-coins"),

    path("wallet/", wallet, name="wallet"),
    path("new-wallet/", new_wallet, name="new-wallet"),
]