from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import NewUser,Foods,Categories

class FoodsSerialier(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields="__all__"


