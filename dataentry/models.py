from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()


    def __str__(self):
        return self.name

class CSVfile(models.Model):
    Date = models.CharField(max_length = 50)
    Area = models.CharField(max_length = 50)
    Customer_Name = models.CharField(max_length = 100)
    ContactNo = models.CharField(max_length =12) 
    Building_Name = models.CharField(max_length = 100)
    Flat_No = models.CharField(max_length = 100)
    C = models.FloatField()
    B = models.FloatField()


    def __str__(self):
        return self.Customer_Name






