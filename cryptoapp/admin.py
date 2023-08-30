from django.contrib import admin
from .models import CryptoCurrency, Wallet, Portfolio
# Register your models here.
admin.site.register(CryptoCurrency)
admin.site.register(Wallet)
admin.site.register(Portfolio)