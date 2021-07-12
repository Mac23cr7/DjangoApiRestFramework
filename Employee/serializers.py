from rest_framework import serializers
from Employee.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('departmentId',
                  'departmenName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employeeId',
                  'employeeName',
                  'department',
                  'dateOfJoin',
                  'photoImg')
