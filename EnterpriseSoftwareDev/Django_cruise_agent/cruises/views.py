from django.shortcuts import render

# Create your views here.
from .models import Cruise, Ship, Cabin

# Create your views here.
def index(request):
    cruises = Cruise.objects.all()
    return render(request, 'cruises/index.html', {'cruises': cruises})