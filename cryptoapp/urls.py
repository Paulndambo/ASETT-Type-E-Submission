from django.urls import path
from cryptoapp.views import add_coins_to_wallet


urlpatterns = [
    path("record-coins/", add_coins_to_wallet, name="record-coins"),
]