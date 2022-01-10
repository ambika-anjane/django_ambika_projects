

# Create your models here.
from django.db import models
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=30)  
    age =  models.IntegerField()  

class Sources(models.Model)  :
    name = models.CharField(max_length=30)  
    column1 = models.CharField(max_length=30,default = 'customer_id')  

'''
class Customers(models.Model):
    Customer_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    
class Orders(models.Model):
    Order_id = models.IntegerField((primary_key = True))
    Customer_id = models.IntegerField()
    order_date = DateField(auto_now=False)
    status  =  models.CharField(max_length=20)  
    credit_card_amount  =  models.IntegerField()
    coupon_amount = models.IntegerField()
    bank_transfer_amount = models.IntegerField()
    gift_card_amount = models.IntegerField()
    amount  = models.IntegerField()

class Payment(models.Model):
    Payment_id = models.IntegerField()
    Payment_method = models.CharField(max_length=30)  
    amount  = models.IntegerField()

''' 


