from django.contrib import admin
from .models import tipo_documento, login_user
# Register your models here.

admin.site.register(tipo_documento)
admin.site.register(login_user)