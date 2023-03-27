from django.urls import path
from . import views

urlpatterns = [
    path('', views.bear_list, name='bears_list'),
    path('bear/<int:id>', views.bear_detail, name= 'bear_detail'),
    # path('edit/<int:id>', views.BearUpdate.as_view(), name='bear_edit'),
    ]