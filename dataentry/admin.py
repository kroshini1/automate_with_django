from django.contrib import admin
from .models import Student,CSVfile,Employee
# Register your models here.
admin.site.register(CSVfile)
admin.site.register(Student)
admin.site.register(Employee)

