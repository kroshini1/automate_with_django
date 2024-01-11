# I want to add some data to the database using custom command
from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "inserting the data into database"


    def handle(self, *args, **kwargs):
        # logic goes here
        dataset = [
            {'roll_no':1002,'name': 'Kiran','age':28},
            {'roll_no':1007,'name': 'amma','age':22},
            {'roll_no':1008,'name': 'nanna','age':31}
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'student with {roll_no} exists already'))
        # #add one data
        self.stdout.write(self.style.SUCCESS('data inserted successfully'))