from django.test import TestCase
import pytest
from cryptoapp.models import Wallet
from django.contrib.auth.models import User

@pytest.mark.django_db
class BaseWalletTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="testuser", 
            email="testuser@gmail.com", 
            first_name="test",
            last_name="user"
        )
        self.wallet = Wallet.objects.create(user=self.user)
        return super().setUp()



class TestWallet(BaseWalletTestCase):
    def test_wallet_exists(self):
        assert self.wallet.user.id == 1