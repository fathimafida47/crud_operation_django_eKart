from django.db import models

# Create your models here.

class EkartAdmin(models.Model):
    username = models.CharField(max_length= 30)
    password = models.CharField(max_length= 25)

    class Meta:
        db_table = "admin_tb"