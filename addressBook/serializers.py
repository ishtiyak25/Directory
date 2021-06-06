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


class AddressSerializer(serializers.ModelSerializer):
    State = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ("HouseNo", "RoadNo", "Name", "State")


class DetailAddressSerializer(serializers.ModelSerializer):
    State = serializers.StringRelatedField()
    Country = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ("HouseNo", "RoadNo", "Name", "State", "Country")