from django.db import models


from eKart_admin.models import Category

# Create your models here.
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




class Product(models.Model):
    product_no = models.CharField(max_length = 50)
    product_name = models.CharField(max_length = 50)
    product_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to = 'product/')
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    status = models.CharField(max_length = 20,default = 'available')

    class Meta:
        db_table = 'product_tb'
 