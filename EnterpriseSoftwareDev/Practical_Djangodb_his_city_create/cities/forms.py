from django import forms
from django.forms import ModelForm
from .models import City

class City_form(ModelForm):
    class Meta:
        model = City
        fields = ('city', 'otherName', 'country', 'latitude', 'longitude', 'year', 'pop')
        labels = {
            # 'id': '',
            'city': 'Enter the new City',
            'otherName': 'Enter the new othername',
            'country': 'Enter the new country',
            'latitude': 'Enter the new latitude value',
            'longitude': 'Enter the new longitude value',
            'year': 'Enter the new year',
            'pop': 'Enter the new pop',
            # 'city_id': '',
        }
        widgets = {
            # 'id': forms.TextInput(attrs=),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}),
            'otherName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'othername'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}),
            'latitude': forms.TextInput(attrs={'class':'form-control', 'placeholder':'lagtitude'}),
            'longitude': forms.TextInput(attrs={'class':'form-control', 'placeholder':'longitude'}),
            'year': forms.TextInput(attrs={'class':'form-control', 'placeholder':'year'}),
            'pop': forms.TextInput(attrs={'class':'form-control', 'placeholder':'pop'}),
            # 'city_id': forms.TextInput(attrs={'class':'form-control'}),
        }