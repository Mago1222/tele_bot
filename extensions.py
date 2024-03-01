import json
import requests
from baza import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException("Невозможно перевести одинаковые валюты")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обрабоать валюту {base}')

        try:
            qoute_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обрабоать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Введите количество правильно')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base_summ = total_base * amount

        return total_base_summ

