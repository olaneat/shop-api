from .models import CartList, Cart
from rest_framework import serializers
from product.models import Product
from register.serializers import UserSerializer


class Cart(serializers.ModelSerializer):
    customer = UserSerializer(read_only =True)
    item = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'customer', 'item', 'created', 'updated')


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartList
        fields = '__all__'