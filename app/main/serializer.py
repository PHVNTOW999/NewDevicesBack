from rest_framework import serializers
from .models import *


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        depth = 1
        fields = "__all__"
