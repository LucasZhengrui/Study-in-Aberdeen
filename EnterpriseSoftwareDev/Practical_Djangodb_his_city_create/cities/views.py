from django.shortcuts import render
from django.core.paginator import Paginator
from .models import City
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from cities.models import City
# Create your views here.

def city_list(request):
        cities = City.cities()
        paginator = Paginator(cities, 50) #show 50 cities per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'cities/city_list.html', {'page_obj': page_obj})

def city__by_name(request, city):
        cities = City.city_by_name(city)
        paginator = Paginator(cities, 50) #show 50 cities per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'cities/city_list.html', {'page_obj': page_obj})

class CityUpdate(UpdateView):
        model = City
        fields = ['id', 'city', 'otherName', 'country', 'latitude', 'longitude', 'year', 'pop', 'city_id']
        success_url = reverse_lazy('city_list')

class CityDelete(DeleteView):
        model = City
        success_url = reverse_lazy('city_list')