from django.core.management.base import BaseCommand

# Propose command = python manage.py greeting Name={dynamic}
# proposed output = Hi {name}, Good Morning
class Command(BaseCommand):
    help = "prints greets or greets the user"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies user given name in command")
        
    def handle(self,*args,**kwargs):
         #write a logic
        name = kwargs['name']
        greeting = f"Hi {name}  Great Good Job"
        self.stdout.write(self.style.SUCCESS(greeting))