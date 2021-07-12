from django.db import models

# Create your models here.

class Departments(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmenName = models.CharField(max_length=100)

class Employees(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    dateOfJoin = models.DateField()
    photoImg = models.CharField(max_length=100)