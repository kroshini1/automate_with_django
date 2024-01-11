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


class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    retirement = models.DecimalField(max_digits=10,decimal_places=2)
    other_benefits = models.DecimalField(max_digits=10,decimal_places=2)
    total_benefits = models.DecimalField(max_digits=10,decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10,decimal_places=2)
    

    def __str__(self):
        return self.employee_name +'-'+ self.designation


