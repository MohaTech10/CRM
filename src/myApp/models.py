from django.db import models

# Create your models here.


class Customer(models.Model):

    name = models.CharField(max_length=200, null=True)  #  false => required
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    # saving  the date that the object is created at


    def __str__(self):
        return self.name  # it must return string value




class Products(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


'''
    1- python3 manage.py makemigrations
    2- python3 manage.py migrate
    3- any property changing must be migrated



'''
