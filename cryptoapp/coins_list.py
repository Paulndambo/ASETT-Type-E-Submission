from cryptoapp.models import CryptoCurrency
coins = [
    {
        'id': 'bitcoin', 
        'symbol': 'btc', 
        'name': 'Bitcoin', 
        'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 
        'current_price': 27937, 
        'market_cap': 543632968292, 
        'market_cap_rank': 1, 
        'fully_diluted_valuation': 586326078322, 
        'total_volume': 18582320766, 
        'high_24h': 27999, 
        'low_24h': 25904, 
        'price_change_24h': 1789.9, 
        'price_change_percentage_24h': 6.84556, 
        'market_cap_change_24h': 34713713800, 
        'market_cap_change_percentage_24h': 6.82107, 
        'circulating_supply': 19470893.0, 
        'total_supply': 21000000.0, 
        'max_supply': 21000000.0, 
        'ath': 69045, 
        'ath_change_percentage': -59.56493, 
        'ath_date': '2021-11-10T14:24:11.849Z', 
        'atl': 67.81, 
        'atl_change_percentage': 41071.96486, 
        'atl_date': '2013-07-06T00:00:00.000Z', 
        'roi': None, 
        'last_updated': '2023-08-29T17:30:56.280Z'
    }, 
    {'id': 'ethereum', 'symbol': 'eth', 'name': 'Ethereum', 'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880', 'current_price': 1735.26, 'market_cap': 208542489029, 'market_cap_rank': 2, 'fully_diluted_valuation': 208542489029, 'total_volume': 12277326805, 'high_24h': 1736.57, 'low_24h': 1639.25, 'price_change_24h': 84.89, 'price_change_percentage_24h': 5.14344, 'market_cap_change_24h': 10205391430, 'market_cap_change_percentage_24h': 5.14548, 'circulating_supply': 120217158.936942, 'total_supply': 120217158.936942, 'max_supply': None, 'ath': 4878.26, 'ath_change_percentage': -64.48095, 'ath_date': '2021-11-10T14:24:19.604Z', 'atl': 0.432979, 'atl_change_percentage': 400083.92862, 'atl_date': '2015-10-20T00:00:00.000Z', 'roi': {'times': 82.06715548096749, 'currency': 'btc', 'percentage': 8206.715548096749}, 'last_updated': '2023-08-29T17:30:52.262Z'}, {'id': 'tether', 'symbol': 'usdt', 'name': 'Tether', 'image': 'https://assets.coingecko.com/coins/images/325/large/Tether.png?1668148663', 'current_price': 1.0, 'market_cap': 82858413494, 'market_cap_rank': 3, 'fully_diluted_valuation': 82858413494, 'total_volume': 20998032908, 'high_24h': 1.002, 'low_24h': 0.986165, 'price_change_24h': 0.00042612, 'price_change_percentage_24h': 0.04263, 'market_cap_change_24h': 71698773, 'market_cap_change_percentage_24h': 0.08661, 'circulating_supply': 82858157223.8269, 'total_supply': 82858157223.8269, 'max_supply': None, 'ath': 1.32, 'ath_change_percentage': -24.40519, 'ath_date': '2018-07-24T00:00:00.000Z', 'atl': 0.572521, 'atl_change_percentage': 74.69951, 'atl_date': '2015-03-02T00:00:00.000Z', 'roi': None, 'last_updated': '2023-08-29T17:30:00.827Z'}, {'id': 'binancecoin', 'symbol': 'bnb', 'name': 'BNB', 'image': 'https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png?1644979850', 'current_price': 229.09, 'market_cap': 35242384880, 'market_cap_rank': 4, 'fully_diluted_valuation': 45812123702, 'total_volume': 602478188, 'high_24h': 232.21, 'low_24h': 216.88, 'price_change_24h': 10.62, 'price_change_percentage_24h': 4.85891, 'market_cap_change_24h': 1634733784, 'market_cap_change_percentage_24h': 4.86417, 'circulating_supply': 153856150.0, 'total_supply': 153856150.0, 'max_supply': 200000000.0, 'ath': 686.31, 'ath_change_percentage': -66.64672, 'ath_date': '2021-05-10T07:24:17.097Z', 'atl': 0.0398177, 'atl_change_percentage': 574784.50907, 'atl_date': '2017-10-19T00:00:00.000Z', 'roi': None, 'last_updated': '2023-08-29T17:30:58.041Z'}, {'id': 'ripple', 'symbol': 'xrp', 'name': 'XRP', 'image': 'https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1605778731', 'current_price': 0.539791, 'market_cap': 28560687869, 'market_cap_rank': 5, 'fully_diluted_valuation': 53975476054, 'total_volume': 1221765921, 'high_24h': 0.543561, 'low_24h': 0.512953, 'price_change_24h': 0.02011675, 'price_change_percentage_24h': 3.87103, 'market_cap_change_24h': 1067207951, 'market_cap_change_percentage_24h': 3.88168, 'circulating_supply': 52914193551.0, 'total_supply': 99988485729.0, 'max_supply': 100000000000.0, 'ath': 3.4, 'ath_change_percentage': -84.13521, 'ath_date': '2018-01-07T00:00:00.000Z', 'atl': 0.00268621, 'atl_change_percentage': 19971.31813, 'atl_date': '2014-05-22T00:00:00.000Z', 'roi': None, 'last_updated': '2023-08-29T17:30:56.517Z'}, {'id': 'usd-coin', 'symbol': 'usdc', 'name': 'USD Coin', 'image': 'https://assets.coingecko.com/coins/images/6319/large/USD_Coin_icon.png?1547042389', 'current_price': 0.999468, 'market_cap': 26050503545, 'market_cap_rank': 6, 'fully_diluted_valuation': 26026683925, 'total_volume': 4621884080, 'high_24h': 1.007, 'low_24h': 0.984177, 'price_change_24h': -0.000890756706595441, 'price_change_percentage_24h': -0.08904, 'market_cap_change_24h': 73365969, 'market_cap_change_percentage_24h': 0.28243, 'circulating_supply': 26037240668.6715, 'total_supply': 26013433175.6996, 'max_supply': None, 'ath': 1.17, 'ath_change_percentage': -14.68371, 'ath_date': '2019-05-08T00:40:28.300Z', 'atl': 0.877647, 'atl_change_percentage': 13.99912, 'atl_date': '2023-03-11T08:02:13.981Z', 'roi': None, 'last_updated': '2023-08-29T17:30:52.920Z'}, {'id': 'staked-ether', 'symbol': 'steth', 'name': 'Lido Staked Ether', 'image': 'https://assets.coingecko.com/coins/images/13442/large/steth_logo.png?1608607546', 'current_price': 1733.26, 'market_cap': 14743461764, 'market_cap_rank': 7, 'fully_diluted_valuation': 14743461764, 'total_volume': 18183345, 'high_24h': 1735.11, 'low_24h': 1638.85, 'price_change_24h': 84.34, 'price_change_percentage_24h': 5.11469, 'market_cap_change_24h': 883235432, 'market_cap_change_percentage_24h': 6.37245, 'circulating_supply': 8506877.93762174, 'total_supply': 8506877.93762174, 'max_supply': 8506877.93762174, 'ath': 4829.57, 'ath_change_percentage': -64.10683, 'ath_date': '2021-11-10T14:40:47.256Z', 'atl': 482.9, 'atl_change_percentage': 258.9769, 'atl_date': '2020-12-22T04:08:21.854Z', 'roi': None, 'last_updated': '2023-08-29T17:30:56.248Z'}, {'id': 'cardano', 'symbol': 'ada', 'name': 'Cardano', 'image': 'https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860', 'current_price': 0.277711, 'market_cap': 9730026148, 'market_cap_rank': 8, 'fully_diluted_valuation': 12493962517, 'total_volume': 301250523, 'high_24h': 0.277836, 'low_24h': 0.260084, 'price_change_24h': 0.01177925, 'price_change_percentage_24h': 4.42943, 'market_cap_change_24h': 413955070, 'market_cap_change_percentage_24h': 4.44345, 'circulating_supply': 35045020830.3234, 'total_supply': 45000000000.0, 'max_supply': 45000000000.0, 'ath': 3.09, 'ath_change_percentage': -91.03314, 'ath_date': '2021-09-02T06:00:10.474Z', 'atl': 0.01925275, 'atl_change_percentage': 1337.71224, 'atl_date': '2020-03-13T02:22:55.044Z', 'roi': None, 'last_updated': '2023-08-29T17:30:57.022Z'}, {'id': 'dogecoin', 'symbol': 'doge', 'name': 'Dogecoin', 'image': 'https://assets.coingecko.com/coins/images/5/large/dogecoin.png?1547792256', 'current_price': 0.066788, 'market_cap': 9400423682, 'market_cap_rank': 9, 'fully_diluted_valuation': 9400390298, 'total_volume': 472888667, 'high_24h': 0.067997, 'low_24h': 0.06243, 'price_change_24h': 0.00348649, 'price_change_percentage_24h': 5.50772, 'market_cap_change_24h': 495382566, 'market_cap_change_percentage_24h': 5.56295, 'circulating_supply': 140791196383.705, 'total_supply': 140790696383.705, 'max_supply': None, 'ath': 0.731578, 'ath_change_percentage': -90.90283, 'ath_date': '2021-05-08T05:08:23.458Z', 'atl': 8.69e-05, 'atl_change_percentage': 76482.29579, 'atl_date': '2015-05-06T00:00:00.000Z', 'roi': None, 'last_updated': '2023-08-29T17:30:58.046Z'}, {'id': 'solana', 'symbol': 'sol', 'name': 'Solana', 'image': 'https://assets.coingecko.com/coins/images/4128/large/solana.png?1640133422', 'current_price': 21.75, 'market_cap': 8878196220, 'market_cap_rank': 10, 'fully_diluted_valuation': 12097989897, 'total_volume': 457026069, 'high_24h': 21.78, 'low_24h': 20.12, 'price_change_24h': 1.16, 'price_change_percentage_24h': 5.61407, 'market_cap_change_24h': 464079356, 'market_cap_change_percentage_24h': 5.51549, 'circulating_supply': 408151069.764791, 'total_supply': 556172379.624223, 'max_supply': None, 'ath': 259.96, 'ath_change_percentage': -91.65386, 'ath_date': '2021-11-06T21:54:35.825Z', 'atl': 0.500801, 'atl_change_percentage': 4232.37295, 'atl_date': '2020-05-11T19:35:23.449Z', 'roi': None, 'last_updated': '2023-08-29T17:30:58.982Z'}]


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