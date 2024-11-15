import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin', 
        'vs_currencies': 'usd,brl'
    }

    try: 
        responce = requests.get(url, params=params)
        responce.raise_for_status()
        data = responce.json()
        return {
            'usd': data['bitcoin']['usd'],
            'brl': data['bitcoin']['brl']
            }
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o preço do Bitcoin: {e}")
        return None

if __name__ == "__main__":
    prices = get_bitcoin_price()
    if prices:
        print("O preço atual do Bitcoin é:")
        print(f"- USD: ${prices['usd']:.2f}")
        print(f"- BRL: R${prices['brl']:.2f}")
    else:
        print("Não foi possivel obter o preço do Bitcoin.")