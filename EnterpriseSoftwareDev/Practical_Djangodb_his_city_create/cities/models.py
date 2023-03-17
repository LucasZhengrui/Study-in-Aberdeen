from django.db import models
from django.conf import settings
# import sqlite3
# Create your models here.

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.TextField()
    otherName = models.TextField()
    country = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    year = models.IntegerField()
    pop = models.IntegerField()
    city_id = models.TextField()

    def __str__(self):
        return f'{self.id}, {self.city}, {self.otherName}, {self.country}, {self.latitude},{self.longitude}, {self.year}, {self.pop}, {self.city_id}'
    
    def cities():
        cities = City.objects.all()
        return cities
    
    def city_by_name(city):
        city_list = City.objects.filter(city=city)
        return city_list
    
    # def update_feature(request, id):
    #     id = City.id
    #     City.city = request.POST.get('name')
