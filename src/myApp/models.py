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


class Tags(models.Model):
    tag_name = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.tag_name

        # // اجهزة الكترونيه

class Products(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name


'''
    1- python3 manage.py makemigrations
    2- python3 manage.py migrate
    3- any property changing must be migrated




    if one USER object has a lot of Orders another object => 80% Foreign key


'''

class Order(models.Model):


    STATUS = (
            ("Pending", "Pending"),
            ("Out for delivery", "Out for delivery"),
            ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.customer.name + " order"
