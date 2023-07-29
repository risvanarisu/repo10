from django.db import models


# Create your models here.

class Admins(models.Model):
   name=models.TextField(max_length=30,db_column='admin_name')
   contact=models.TextField(max_length=30,db_column='admin_contact')
   email=models.TextField(max_length=30,db_column='admin_email')
   username=models.TextField(max_length=30,db_column='admin_username')
   password=models.TextField(max_length=30,db_column='admin_password')
   

   class Meta:
        db_table='admins'
        
