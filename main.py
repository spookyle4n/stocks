import requests

api_key = 'Q3syD1gaoZ0SlrafEc7vQyYQCOjJzPUY'  # Replace with your actual Polygon.io API key

def get_stock_info(symbol):
    base_url = 'https://api.polygon.io/v2/reference/tickers'
    params = {
        'ticker': symbol,
        'apiKey': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        stock = data['results'][0]
        print('Company Name:', stock['name'])
        print('Exchange:', stock['market'])
        print('Country:', stock['country'])
        print('Stock Type:', stock['type'])
        print('Market Cap:', stock['marketCap'])
        print('Description:', stock['description'])
    else:
        print('No information found for the given stock symbol.')

def main():
    symbol = input('Enter the stock symbol: ')
    get_stock_info(symbol)

if __name__ == '__main__':
    main()
