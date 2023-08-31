

def load_coins():
    coins_list = []
    for x in coins:
        coins_list.append(
            CryptoCurrency(
            name=x['name'],
            symbol=x['symbol'],
            current_price=x['current_price'],
            quantity_available=x['total_supply'] 
            )
        )

    CryptoCurrency.objects.bulk_create(coins_list)