from django.core.management.base import BaseCommand
from rides.models import Rider, Driver

class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        if Rider.objects.count() == 0:
            Rider.objects.create(name="R1")
            Rider.objects.create(name="R2")
            Rider.objects.create(name="R3")
            
        if Driver.objects.count() == 0:
            Driver.objects.create(name="D1", latitude=12.9, longitude=77.5, is_available=True)
            Driver.objects.create(name="D2", latitude=13.0, longitude=76.6, is_available=True)
            Driver.objects.create(name="D3", latitude=14.0, longitude=75.6, is_available=True)
            Driver.objects.create(name="D4", latitude=15.0, longitude=74.6, is_available=True)
            Driver.objects.create(name="D5", latitude=16.0, longitude=73.6, is_available=True)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))