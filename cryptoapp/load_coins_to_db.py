import requests

coinGeckoURL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&locale=en"

res = requests.get(coinGeckoURL)

coins_data = res.json()
print(coins_data)