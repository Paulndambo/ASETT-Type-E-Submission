from django.db import models

from django.contrib.auth.models import User
from core.models import AbstractBaseModel

import uuid

# Create your models here.
class CryptoCurrency(AbstractBaseModel):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Wallet(AbstractBaseModel):
    wallet_id = models.UUIDField(default=uuid.uuid4())
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class Portfolio(AbstractBaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="portfolios")
    currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE, related_name="coins")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    coin_total_value = models.DecimalField(max_digits=50,decimal_places=2, default=0)

    def __str__(self):
        return f"{self.wallet.user.username} added {self.currency.name} to wallet"


class Transaction(AbstractBaseModel):
    send_from = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="coinssend")
    send_to = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="coinsreceived")
    currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    status = models.CharField(max_length=255, null=True)