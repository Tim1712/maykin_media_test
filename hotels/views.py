from django.shortcuts import render
from .models import Hotel, City
from django.http import HttpResponse
from cron.functions import load_data
# Create your views here.

def home(request):
    context = City.objects.all()
    return render(request, 'hotels/home.html', {"cities": context})


def results(request):
    city_id = request.GET['CitySelection']
    city = City.objects.filter(id=city_id)[0]
    context = Hotel.objects.filter(city=city)
    return render(request, 'hotels/results.html', {'hotels': context})

