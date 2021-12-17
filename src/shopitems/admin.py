from django.contrib import admin
from .models import Product, Role, Order, Client

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Role)

