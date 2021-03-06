from django.db import models


# database for the cities
class City(models.Model):
    city = models.CharField(max_length=100)
    abb = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.city} ({self.abb})'


# Database for the hotels, connected with cities
class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    hotel_city_abb = models.CharField(max_length=10, default=0)
    hotel = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.hotel} in {self.city}'

