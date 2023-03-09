from django.contrib import admin
from .models import Cities, Countries


# Register your models here.
# admin.site.register(Cities)
@admin.register(Countries)
class  CountriesModel(admin.ModelAdmin):
    list_filter = ('countryName', 'phone_code')
    list_display = ('countryName', 'phone_code')


# admin.site.register(Countries)
@admin.register(Cities)
class CitiesModel(admin.ModelAdmin):
    list_filter = ('name', 'country')
    list_display = ('name', 'country')
