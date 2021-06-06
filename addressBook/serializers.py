from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("Name", "Latitude", "Longitude", "Code")


class StateSerializer(serializers.ModelSerializer):
    Country = serializers.StringRelatedField()

    class Meta:
        model = State
        fields = ("Country", "Name",)
