from django.contrib import admin
from .models import CryptoCurrency, Wallet, Portfolio
# Register your models here.
@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ["symbol", "name", "current_price"]

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["wallet_id", "phone_number", "referral_code", "invited_by"]

admin.site.register(Portfolio)