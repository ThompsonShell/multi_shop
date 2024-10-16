import os

import requests

RANDOM_CAT_IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'


def random_image_url():
    return requests.get(url=RANDOM_CAT_IMAGE_URL).json()[0]['url']


def random_image_download(dir_address: str) -> str:
    image_url = random_image_url()
    image_name = image_url.split('/')[-1]

    if not os.path.exists(dir_address):
        os.makedirs(dir_address)

    with open(os.path.join(dir_address, image_name), 'wb') as image:
        image.write(requests.get(image_url).content)

    return image_name


url = "https://api.thecatapi.com/v1/images/search"
response = requests.get(url)

# Status kodni tekshirish
print(f"Status code: {response.status_code}")

# Javobni matn shaklida ko'rish
print("Response text:", response.text)

# JSONni dekodlashga urinish
try:
    data = response.json()
    print("JSON data:", data)
except ValueError as e:
    print("Failed to decode JSON:", e)
