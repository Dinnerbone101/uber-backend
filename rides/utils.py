from .models import Rider, Ride, Driver
import math

def dist(lat1,lat2,lon1,lon2):
    d = (lat1-lat2)**2 + (lon1-lon2)**2
    return math.sqrt(d)


def get_nearest_driver(pickup_lat,pickup_lon):
     
     drivers = Driver.objects.filter(is_available = True)


     nearest_driver = None
     min_dist = 1e9

     for driver in drivers:
        distance = dist(driver.latitude,pickup_lat,driver.longitude,pickup_lon)

        if distance < min_dist:
            min_dist = distance
            nearest_driver = driver

     return nearest_driver