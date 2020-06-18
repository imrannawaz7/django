from django.db import models

# Create your models here.
class Name(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)

class ID(models.Model):
    userID=models.IntegerField(max_length=10)


class Contact(models.Model):
    area_code = models.IntegerField(max_length=7)
    phone=models.IntegerField(max_length=7)
    address=models.CharField(max_length=50)
