from django.db import models
from django.contrib.auth.models import User
from . import Roles


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(null=True, default='Добавь описание')
    photo = models.FileField(verbose_name='Photo', blank=True)
    discount = models.FloatField(default=0.5)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}  {self.price}"


class Order(models.Model):
    customer = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(to=Product)
    is_active = models.BooleanField(default=True)


class Role(models.Model):
    name = models.CharField(choices=Roles.choices, max_length=10)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user}  {self.role}"


