from rest_framework import serializers
from .models import *


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        depth = 1
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        depth = 1
        fields = "__all__"


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        depth = 2
        fields = "__all__"
