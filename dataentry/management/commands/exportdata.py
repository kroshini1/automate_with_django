import csv
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import datetime

# proposed command = python manage.py exportdata model_name

class Command(BaseCommand):
    help = "export data from database  to CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="give the name of model")

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()
        # search through all the installed apps for the model
        model=None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break # stop executing once model is found
            except LookupError:
                pass
        if not model:
            self.stdout.write(self.style.WARNING(f"Model {model_name} could not found"))
            return
        
        #fetch the data from the database
        data = model.objects.all()

        #generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # define the csv file name/path
        file_path = f" exported {model_name}_data_{timestamp}.csv"
        


        #open the csv file and write the data
        with open(file_path, 'w', newline='')as file:
            writer = csv.writer(file)

            # write the csv header
            # we want the print field names of model that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])

            # WRITE data rows
            for csvs in data:
                writer.writerow([getattr(csvs, field.name)for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS('Data exported Successfully!'))