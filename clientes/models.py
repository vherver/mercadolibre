from django.db import models
import uuid
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Client(models.Model, ):
    """
    Clase para realizar el registro de tokens de usuario, codigo de autorizacion y refresh tokens
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    code = models.CharField(max_length=256, blank=False, null=False)
    access_token = models.CharField(max_length=256)
    token_type = models.CharField(max_length=25, default="")
    refresh_token = models.CharField(max_length=256)
    mercado_libre_user_id = models.CharField(max_length=25, default="")
    expiration_date = models.DateTimeField(blank=True, null=True)