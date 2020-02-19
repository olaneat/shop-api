from rest_framework import serializers
from register.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'location', 'phone_number')
        


