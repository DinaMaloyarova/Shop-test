from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ('description', )
        fields = read_only_fields + (
            'id', 'name', 'price', 'photo',
        )

    def validate(self, attrs):
        if attrs['price'] <= 0:
            raise ValidationError('Некорректное значение цены')
        return attrs


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'description',
        )


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()

    class Meta:
        fields = 'username'


class OrderSerializer(serializers.Serializer):
    product = ProductDetailSerializer(many=True)
    customer = UserSerializer()

    class Meta:
        fields = (
            'id', 'product', 'customer',
        )


class EmailSerializer(serializers.Serializer):
    email = serializers.CharField()
    message = serializers.CharField()