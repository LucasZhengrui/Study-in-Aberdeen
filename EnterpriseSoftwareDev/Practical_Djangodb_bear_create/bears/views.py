from django.shortcuts import render, get_object_or_404
from .models import Bear, Sighting
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.
def bear_list(request):
    bears = Bear.objects.all()
    return render(request, 'bears/bear_list.html', {'bears' : bears})

def bear_detail(request, id):
    # bears = get_object_or_404(Bear, id=id)
    sightings = Sighting.objects.filter(bear_id=id)
    return render(request, 'bears/bear_detail.html', {'sightings' : sightings})

class BearUpdate(UpdateView):
    model = Sighting
    fields = ['bear_id', 'deploy_id', 'recieved', 'latitude', 'longitude', 'temperature', 'created_date']
    success_url = reverse_lazy('bear_detail')