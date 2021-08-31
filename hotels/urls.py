from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hotels-home'),
    path('results/', views.results, name='hotels-results'),
]
