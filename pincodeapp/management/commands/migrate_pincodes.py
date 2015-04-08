import csv
from django.core.management.base import BaseCommand
from pincodeapp.models import PinCodeDirectory

class Command(BaseCommand):
    help = 'Migrate pincodes for first time'

    def handle(self, *args, **options):
        with open('pincodeapp/data/all_india_pin_code.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = spamreader.next()
            for row in spamreader:
                pincode = PinCodeDirectory(
                                 office_name=row[0],
                                 pincode=row[1],
                                 office_type=row[2],
                                 delivery_status=row[3],
                                 division_name=row[4],
                                 region_name=row[5],
                                 circle_name=row[6],
                                 taluk=row[7],
                                 district_name=row[8],
                                 state_name=row[9]
                                 )
                pincode.save()