import requests

from datetime import date


GET_CURRENCY_URL = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{date}'

today = date.today()


currency_list = ['USD', 'RUB']
for curr in currency_list:
    response = requests.get(url=GET_CURRENCY_URL.format(currency=curr, date=today)).json()[0]
    print(response['Ccy'], response['Rate'])