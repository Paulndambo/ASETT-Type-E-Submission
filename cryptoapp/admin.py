from django.contrib import admin
from .models import CryptoCurrency, Wallet
# Register your models here.
admin.site.register(CryptoCurrency)
admin.site.register(Wallet)