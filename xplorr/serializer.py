from .models import Country, City, Goals, Profile, Accomodation, Sightseeing
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = '__all__'

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = '__all__'

class SightseeingSeriializer(serializers.ModelSerializer):
    class Meta:
        model = Sightseeing
        fields = '__all__'