from django.contrib import admin
from .models import Client, Package, Carrier

admin.site.register(Carrier)
admin.site.register(Client)
admin.site.register(Package)