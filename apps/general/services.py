import os
from http.client import responses

import requests

RANDOM_CAT_IMAGE_URL = 'https://api.thecatapi.com/v1/images/search'


def random_image_url():
    while (response :=requests.get(url=RANDOM_CAT_IMAGE_URL)).status_code != 200:
        pass
    return response.json()[0]['url']


def random_image_download(dir_address: str) -> str:
    image_url = random_image_url()
    image_name = image_url.split('/')[-1]

    if not os.path.exists(dir_address):
        os.makedirs(dir_address)

    with open(os.path.join(dir_address, image_name), 'wb') as image:
        image.write(requests.get(image_url).content)

    return image_name


