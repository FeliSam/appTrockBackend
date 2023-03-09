from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CitiesViewSet, CountriesViewSet

router = routers.DefaultRouter()
router.register(r'Countries', CountriesViewSet)
router.register(r'Cities', CitiesViewSet)

urlpatterns = [
    path('countrystate/', include(router.urls)),
]