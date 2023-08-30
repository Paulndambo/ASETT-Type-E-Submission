from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from cryptoapp.models import CryptoCurrency, Wallet, Portfolio

# Create your tests here.
class CryptoCurrencyTestCase(TestCase):
    def setUp(self) -> None:
        CryptoCurrency.objects.create(
            name="Bitcoin",
            symbol="btc",
            current_price=27937.0,
            quantity_available=21000000.0
        )



        return super().setUp()


    def test_bitcoin_created_successfully(self):
        bitcoin = CryptoCurrency.objects.get(name="Bitcoin")
        self.assertEqual(bitcoin.name, "Bitcoin")
        self.assertEqual(bitcoin.symbol, "btc")