#Simple script to grab data on BTC price
import datetime
import requests

date = datetime.date.today()
print("What is the price of BTC and ETH on todays date? ", date)
url = 'https://api.coingecko.com/api/v3/simple/price'
params = {'ids': 'bitcoin,ethereum', 'vs_currencies': 'usd'}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    data = response.json()
    bitcoin_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    print("\nThe price of btc in usd is ", bitcoin_price)
    print("\nThe price of eth in usd is ", eth_price)
except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")