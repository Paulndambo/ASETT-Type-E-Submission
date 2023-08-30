from django.test import TestCase
import pytest

from decimal import Decimal

from cryptoapp.models import CryptoCurrency


@pytest.mark.django_db
class BaseCryptoCurrencyTestCase(TestCase):
    def setUp(self) -> None:
        self.currency = CryptoCurrency.objects.create(
            name="Bitcoin",
            symbol="btc",
            current_price=27937.0,
            quantity_available=21000000.0
        )

        return super().setUp()


class TestCryptoCurrencies(BaseCryptoCurrencyTestCase):
    def test_cryptocurrency_symbol(self):
        assert self.currency.symbol == "btc"
        
    def test_currency_name(self):
        assert self.currency.name.lower() == "bitcoin"
        assert self.currency.name == "Bitcoin"

    def test_currency_price_is_decimal(self):
        assert self.currency.current_price == Decimal(27937)
        