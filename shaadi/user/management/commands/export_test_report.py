from django.core.management.base import BaseCommand
from user.models import CustomUser
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
    
        with open('report.csv', 'w') as csvfile:
          
            writer = csv.writer(csvfile)
     
            writer.writerow(['users','subscribed users'])
            
            users = CustomUser.objects.all().count()
            subscribed = CustomUser.objects.filter(is_subscribed=True).count()
        
     
            writer.writerow([users,subscribed])