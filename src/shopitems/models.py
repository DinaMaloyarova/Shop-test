from django.db import models
from django.contrib.auth.models import User
import base64


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(null=True, default='Добавь описание')
    photo = models.ImageField(upload_to='images/', verbose_name='Photo', blank=True)
    discount = models.FloatField(default=0.5)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}  {self.price}"

    @property
    def photo_base64(self):
        with open(self.photo.url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return image_data

    @property
    def photo_path(self):
        return self.photo.url

class Order(models.Model):
    customer = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(to=Product)
    is_active = models.BooleanField(default=True)


class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customer')
    role = models.CharField(default="CLIENT", max_length=50)

