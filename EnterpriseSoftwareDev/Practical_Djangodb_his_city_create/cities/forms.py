from django import forms
from django.forms import ModelForm
from .models import City

class City_form(ModelForm):
    class Meta:
        model = City
        fields = ('id', 'city', 'otherName', 'country', 'latitude', 'longitude', 'year', 'pop', 'city_id')
        