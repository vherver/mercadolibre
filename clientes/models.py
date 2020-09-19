from django.db import models
import uuid


class Client(models.Model):
    """
    Clase para realizar el registro de tokens de usuario, codigo de autorizacion y refresh tokens
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=256, blank=False, null=False)
    code = models.CharField(max_length=256, blank=False, null=False)
    token = models.CharField(max_length=256)
    refresh_token = models.CharField(max_length=256)
    expiration_date = models.DateTimeField