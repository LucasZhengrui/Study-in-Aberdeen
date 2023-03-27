from django.urls import path
from . import views

urlpatterns = [
    path('', views.bear_list, name='bears_list'),
    path('bear/<int:id>/', views.bear_detail, name= 'bear_detail'),
    path('bear_new/', views.bear_new, name = 'bear_new'),
    path('bear/<int:id>/edit/', views.bear_edit, name='bear_edit'),
    path('bear/<int:id>/delete/', views.bear_delete, name='bear_delete'),
    ]