from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Country, City, Goals, Profile, Accomodation, Sightseeing, Category
from .serializer import CountrySerializer, CitySerializer, GoalsSerializer, AccomodationSerializer,SightseeingSeriializer,CategoriesSerializer
# Create your views here.

#ALl countries
class allCountry(APIView):
    def get(Self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
#All cities
class allCities(APIView):
    def get(Self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

#all goals
class allGoals(APIView):
    def get(Self, request):
        goals = Goals.objects.all()
        serializer = GoalsSerializer(goals, many=True)
        return Response(serializer.data)

#get accommodations
class allAccomodations(APIView):
    def get(Self, request):
        accom = Accomodation.objects.all()
        serializer = AccomodationSerializer(accom, many=True)
        return Response(serializer.data)

#get Sight seeing places
class allSightSeeing(APIView):
    def get(Self, request):
        sight = Sightseeing.objects.all()
        serializer = CountrySerializer(sight, many=True)
        return Response(serializer.data)

#get all categories
class allCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)