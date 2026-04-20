from django.http import JsonResponse
from .models import Rider, Ride, Driver
from .utils import *
import json

def create_ride(request):
        
        if request.method != "POST":
            return JsonResponse({"error": "Only POST allowed"})

        rider = Rider.objects.first()
        data = json.loads(request.body)

        

        ride = Ride.objects.create(
            rider=rider,
            driver=None,
            pickup_lat=data["pickup_lat"],
            pickup_lon=data["pickup_lon"],
            drop_lat=data["drop_lat"],
            drop_lon=data["drop_lon"],
            status="REQUESTED",
            fare= 0
        )

        driver = get_nearest_driver(ride.pickup_lat,ride.pickup_lon)
        driver.save()

        if not driver:
            return JsonResponse({"error": "No drivers available"})
        
        driver.is_available = False
        driver.save()

        ride.status = "ASSIGNED"
        ride.driver = driver
        ride.fare= 30 + (dist(ride.pickup_lat,ride.drop_lat,ride.pickup_lon,ride.drop_lon))*10
        ride.save()

        return JsonResponse({
        "message": "Ride created",
        "ride_id": ride.id
        })




def start_ride(request, ride_id):

    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"})
        
    try:
        ride = Ride.objects.get(id=ride_id)


        if ride.status != "ASSIGNED":
            return JsonResponse({"error": "Ride cannot be started"})

        ride.status = "ONGOING"
        ride.save()  

        return JsonResponse({"message": "Ride started"})

    except Ride.DoesNotExist:
        return JsonResponse({"error": "Ride not found"})
    

def complete_ride(request,ride_id):

    if request.method != "POST":
         return JsonResponse({"error": "Only POST allowed"})
    try:
        ride = Ride.objects.get(id=ride_id)
        driver = ride.driver

        ride.status = "COMPLETED"
        ride.save()

        driver.is_available = True
        driver.latitude = ride.drop_lat
        driver.longitude = ride.drop_lon
        driver.save()

        return JsonResponse({"message": "Ride completed"})

    except Ride.DoesNotExist:
         return JsonResponse({"error": "Ride not found"})
    
    
def cancel_ride(request,ride_id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"})
    try:
         ride = Ride.objects.get(id = ride_id)
         driver = ride.driver

         ride.status = "CANCELLED"
         ride.save()

         driver.is_available = True
         driver.save()

         return JsonResponse({"message" : "Ride Cancelled"})
    
    except Ride.DoesNotExist:
         return JsonResponse({"error": "Ride not found"})
    

