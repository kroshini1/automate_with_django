from django.core.management.base import BaseCommand, CommandError
from dataentry.models import CSVfile
import csv
from django.apps import apps

# propose command - python manage.py import data file_path model_name
class Command(BaseCommand):
    help = " Import the data from csv files"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str,help="path to the csv file")
        parser.add_argument('model_name',type=str,help='name of the model')
    
    def handle(self, *args, **kwargs):
        #logic goes here
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        # search for the model across all installed apps
        model= None
        for app_config in apps.get_app_configs():
            #try to search for the model
            try:
                model = apps.get_model(app_config.label,model_name)
                break #stop searching once model is found
            except LookupError:
                continue #model not found continue searching in next app

        if not model:
            raise CommandError(f'model {model_name} not found in any app!')


        with open(file_path,'r')as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully'))

