from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .utils import create_token


def user_regitration(request):
    if request.method == "GET":
        token_data = create_token(code=request.GET["code"])
        client = Client.objects.create(code=request.GET["code"],
                                       token_type=token_data["token_type"],
                                       access_token=token_data["access_token"],
                                       refresh_token=token_data["refresh_token"],
                                       mercado_libre_user_id=token_data["user_id"],
                                       )
        return HttpResponse("Gracias por Registrarse en nuestra aplicacion")