from hotels.models import Hotel, City
import os
import csv
import pandas

def load_data():

    """
    First I tried to connect with the HTTP Basic Authentication but unfortunately didn't succeed
    I tried to connect with "r = requests.get('http://python-demo.maykin.nl/', auth=('python-demo', 'claw30_bumps'))"
    and other ways but kept getting error code 401

    So instead of the basis authentication I made a Cronjob which runs this function every 30 minutes.
    It checks if there is something new added to the CSV files. if so, he adds the new data to the database.
    """

    # Read the CSV files
    city_data = pandas.read_csv('cron/city.csv', sep=';', header=None)
    hotel_data = pandas.read_csv('cron/hotel.csv', sep=';', header=None)

    # Check if all the cities are in the database, If not add new city.
    for row in city_data.values:
        if not City.objects.filter(city=row[1]).exists():
            data = City(city=row[1], abb=row[0])
            data.save()

    # Check if all the hotels are in the database, If not add new hotel.
    for row in hotel_data.values:
        if not Hotel.objects.filter(hotel_city_abb=row[1], hotel=row[2]).exists():
            # Check if the city of the new hotel is available. If so, add new hotel.
            if City.objects.filter(abb=row[0]).exists():
                city = City.objects.get(abb=row[0])
                data = Hotel(city=city, hotel_city_abb=row[1], hotel=row[2])
                data.save()
            # If city of the hotel not exists, add unknown city with abb and add hotel.
            else:
                data = City(city="unknown", abb=row[0])
                data.save()
                city = City.objects.get(city="unknown", abb=row[0])
                data = Hotel(city=city, hotel_city_abb=row[1], hotel=row[2])
                data.save()



