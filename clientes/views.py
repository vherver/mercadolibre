from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .utils import create_token, refresh_token
from datetime import timedelta, datetime


def user_regitration(request):
    if request.method == "GET":
        token_data = create_token(code=request.GET["code"])

        defaults = {
            "access_token": token_data["access_token"],
            "refresh_token": token_data["refresh_token"],
            "expiration_date": datetime.now() + timedelta(seconds=token_data["expires_in"]),
            "code": request.GET["code"],
            "token_type": token_data["token_type"],
        }

        try:
            obj = Client.objects.get(mercado_libre_user_id=token_data["user_id"])
            for key, value in defaults.items():
                setattr(obj, key, value)
            obj.save()
        except Client.DoesNotExist:
            new_values = {"mercado_libre_user_id": token_data["user_id"]}
            new_values.update(defaults)
            obj = Client(**new_values)
            obj.save()

        return HttpResponse("Gracias por Registrarse en nuestra aplicacion")


def action(request):
    client = Client.objects.get(id="791dfe8122104d508d6df2a4cfbadc60")
    client = refresh_token(client)
    return HttpResponse("Gracias por Registrarse en nuestra aplicacion")


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def nofitication(request):
    print(123456)
    return HttpResponse("OK")