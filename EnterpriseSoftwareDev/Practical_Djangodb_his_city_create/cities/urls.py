from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('cities/<str:city>', views.city__by_name, name='cityname'),
    path('edit_cities/<str:city>', views.city_edit, name='city_edit'),
    ]