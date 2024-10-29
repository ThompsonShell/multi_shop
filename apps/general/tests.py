import requests

from datetime import date


GET_CURRENCY_URL = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

today = date.today()

response = requests.get
