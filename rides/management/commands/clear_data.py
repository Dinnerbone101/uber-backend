from django.core.management.base import BaseCommand
from rides.models import Rider, Driver, Ride

class Command(BaseCommand):
    help = "Clear all data"

    def handle(self, *args, **kwargs):
        Ride.objects.all().delete()
        Driver.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All data cleared"))