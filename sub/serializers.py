from .models import Subscription
from rest_framework import serializers
from register.models import CustomUser


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ('id',)