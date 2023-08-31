import requests
from decimal import Decimal
from cryptoapp.models import CryptoCurrency

coinGeckoURL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&locale=en"

res = requests.get(coinGeckoURL)

coins_data = res.json()

def get_coins_to_update():
    existing_coins = list(CryptoCurrency.objects.values_list('symbol', flat=True))

    print(existing_coins)
    return
    coins_to_update = [{
        "name": x["name"],
        "symbol": x["symbol"],
        "current_price": x["current_price"],
        "total_supply": x["total_supply"]
    } for x in coins_data if x['symbol'] in existing_coins]

    for x in coins_to_update:
        currency = CryptoCurrency.objects.get(symbol=x['symbol'])
        currency.quantity_available = x['total_supply']
        currency.current_price = x['current_price']
        currency.save()

        related_portfolios = currency.coins.all()
        if related_portfolios:
            for portfolio in related_portfolios:
                portfolio.coin_total_value = Decimal(portfolio.amount) * Decimal(currency.current_price)
                portfolio.save()

    #return coins_to_update
