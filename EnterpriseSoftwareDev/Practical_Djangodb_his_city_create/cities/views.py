from django.shortcuts import render
from django.core.paginator import Paginator
from .models import City
import pymysql
from .forms import City_form
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

def city_edit(request, city):
        update_stuff = City.objects.get(pk = city)
        form = City_form
        return render(request, 'cities/edit.html', {'form': form})

# def data_insert(request):
#         if request.method == 'GET':
#                 return render(request, 'cities/edit.html')
#         else:
#                 input_value = request.POST.get('title')
#                 connection = pymysql.connect(host = '127.0.0.1', port = 8000, db = 'db.sqlite3', charset = 'utf8')
#                 cursor = connection.cursor(cursor = pymysql.cursors.DictCursor)

                # cursor.execute('insert')