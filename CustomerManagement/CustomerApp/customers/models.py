from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    name = models.CharField(max_length=200, null=False)
    account_no = models.PositiveIntegerField(default=1, primary_key=True, unique=True, auto_created=True)
    date_of_birth = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    balance = models.IntegerField(default=0)


class Customer(models.Model):
    pass