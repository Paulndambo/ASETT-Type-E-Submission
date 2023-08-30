from django.dispatch import receiver
from django.db.models.signals import post_save
from cryptoapp.models import Wallet
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_wallet_when_user_signs_up(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)