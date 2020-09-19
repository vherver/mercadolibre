import requests
import json
from django.conf import settings


def create_token(code):
    url = settings.MERCADOLIBRE_AUTH_URL

    payload = f'grant_type=authorization_code&client_id={settings.MERCADOLIBRE_CLIENT}' \
              f'&client_secret={settings.MERCADOLIBRE_CLIENT_SECRET}' \
              f'&code={code}' \
              f'&redirect_uri={settings.MERCADOLIBRE_REDIRECT_URI}'

    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)
