from hotels.models import Hotel, City
import os
import csv
import pandas

def load_data():

    """
    Authentication uitleg
    """

    city_data = pandas.read_csv('cron/city.csv', sep=';', header=None)
    hotel_data = pandas.read_csv('cron/hotel.csv', sep=';', header=None)

    for row in city_data.values:
        if not City.objects.filter(city=row[1]).exists():
            data = City(city=row[1], abb=row[0])
            data.save()

    for row in hotel_data.values:
        if not Hotel.objects.filter(hotel_city_abb=row[1], hotel=row[2]).exists():
            if City.objects.filter(abb=row[0]).exists():
                city = City.objects.get(abb=row[0])
                data = Hotel(city=city, hotel_city_abb=row[1], hotel=row[2])
                data.save()

            else:
                print('The city of your hotel does not exist in database, please add city first')


