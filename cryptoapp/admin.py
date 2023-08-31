from django.contrib import admin
from .models import CryptoCurrency, Wallet, Portfolio
# Register your models here.
@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ["symbol", "name", "current_price"]

admin.site.register(Wallet)
admin.site.register(Portfolio)