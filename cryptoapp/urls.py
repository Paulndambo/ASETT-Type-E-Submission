from django.urls import path
from cryptoapp.views import (
    add_coins_to_wallet, new_wallet, wallet, 
    failed_wallet_transaction, transfer_coins
)


urlpatterns = [
    path("record-coins/", add_coins_to_wallet, name="record-coins"),

    path("wallet/", wallet, name="wallet"),
    path("new-wallet/", new_wallet, name="new-wallet"),
    path("transfer-coins/", transfer_coins, name="transfer-coins"),
    path("failed-transaction/", failed_wallet_transaction, name="failed-transaction"),
]