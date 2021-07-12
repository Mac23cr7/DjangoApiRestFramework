# Generated by Django 3.2.5 on 2021-07-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False)),
                ('departmenName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeId', models.AutoField(primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('dateOfJoin', models.DateField()),
                ('photoImg', models.CharField(max_length=100)),
            ],
        ),
    ]
