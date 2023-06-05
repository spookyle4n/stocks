import requests
import time

api_key = 'BQKDP85SFSMOP3PM'  # Replace with your actual Alpha Vantage API key

def get_stock_price(symbol):
    base_url = 'https://www.alphavantage.co/query'
    function = 'GLOBAL_QUOTE'
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key
    }

    while True:
        response = requests.get(base_url, params=params)
        data = response.json()

        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            price = stock_data['05. price']
            print('Stock Symbol:', symbol)
            print('Price:', price)
        else:
            print('No information found for the given stock symbol.')

        time.sleep(5)  # Delay between each request (5 seconds in this example)

def main():
    symbol = input('Enter the stock symbol: ')
    get_stock_price(symbol)

if __name__ == '__main__':
    main()
