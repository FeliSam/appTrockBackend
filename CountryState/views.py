from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CitiesSerializer, CountriesSerializer
from .models import Cities, Countries

# Create your views here.
class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer