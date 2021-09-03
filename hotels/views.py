from django.shortcuts import render
from .models import Hotel, City
from django.http import HttpResponse
from cron.functions import load_data
# Create your views here.


# Function for adding a new hotel/city to database
def add_hotel(request):
    city_name = request.POST["city_name"].capitalize()
    hotel_name = request.POST["hotel_name"]
    city_abb = city_name[:3].upper()

    # Check if city exist, if not add city first
    if not City.objects.filter(city=city_name, abb=city_abb).exists():
        data = City(city=city_name, abb=city_abb)
        data.save()

    # Add new hotel to database
    city = City.objects.filter(city=city_name)[0]
    total_hotels = len(Hotel.objects.filter(city=city)) + 1
    data = Hotel(city=city, hotel_city_abb=f"{city_abb}{total_hotels}", hotel=hotel_name)
    data.save()


def home(request):
    # Post request for adding a new hotel
    if request.method == 'POST':
        add_hotel(request)

    # Create variables necessary for page and render
    context = City.objects.all()
    return render(request, 'hotels/home.html', {"cities": context})


def results(request):
    # Post request for adding a new hotel
    if request.method == 'POST':
        add_hotel(request)

    # Create variables necessary for page and render
    city_id = request.GET['CitySelection']
    city = City.objects.filter(id=city_id)[0]
    context = Hotel.objects.filter(city=city)
    context2 = City.objects.all()
    context3 = City.objects.filter(id=city_id)
    print(context3)

    return render(request, 'hotels/results.html', {'hotels': context,
                                                   "cities": context2,
                                                   "current_city": context3})
