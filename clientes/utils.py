import requests
import json
from django.conf import settings
from datetime import timedelta, datetime


def create_token(code):
    url = settings.MERCADOLIBRE_AUTH_URL

    payload = f'grant_type=authorization_code' \
              f'&client_id={settings.MERCADOLIBRE_CLIENT}' \
              f'&client_secret={settings.MERCADOLIBRE_CLIENT_SECRET}' \
              f'&code={code}' \
              f'&redirect_uri={settings.MERCADOLIBRE_REDIRECT_URI}'

    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


def refresh_token(client):
    url = settings.MERCADOLIBRE_AUTH_URL

    payload = f'grant_type=refresh_token' \
              f'&client_id={settings.MERCADOLIBRE_CLIENT}' \
              f'&client_secret={settings.MERCADOLIBRE_CLIENT_SECRET}' \
              f'&refresh_token={client.refresh_token}'

    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response = json.loads(response.text)

    client.access_token = response['access_token']
    client.refresh_token = response['refresh_token']
    client.expiration_date = datetime.now() + timedelta(response['expires_in'])
    client.save()

    return client

