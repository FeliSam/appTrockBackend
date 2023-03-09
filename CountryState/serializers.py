from rest_framework import serializers
from .models import Cities, Countries

class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ['countryID', 'countryName', 'countryValue', 'phone_code', 'currency', 'region', 'latitude', 'longitude', 'emoji', 'date']


class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = ['citiesID', 'name', 'latitude', 'longitude', 'country']
