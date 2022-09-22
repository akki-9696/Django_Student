from django.db import models



class Student_Info(models.Model):
    # enter the fields required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    DOB = models.DateField()
    City = models.CharField(max_length=100)


class Parent_Info(models.Model):
    # enter the fields required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)



