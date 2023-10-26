from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'customer_tb'
    
   
class Seller(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    company_name =models.CharField(max_length = 20)
    bank_name = models.CharField(max_length = 20)
    bank_branch = models.CharField(max_length = 20)
    IFSC = models.CharField(max_length = 20)
    picture = models.ImageField(upload_to = 'seller/')
    account_number = models.CharField(max_length = 20)
    loginid = models.CharField(max_length = 20)
    status = models.CharField(max_length = 50,default='pending')


    class Meta:
        db_table = 'seller_tb'





 
