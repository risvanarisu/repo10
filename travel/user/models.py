from django.db import models

# Create your models here.


class Users(models.Model):
    first_name=models.TextField(max_length=30,db_column='f_name')
    last_name=models.TextField(max_length=30,db_column='l_name')
    gender=models.CharField(max_length=6,db_column='gender')
    dateofbirth=models.DateField(db_column='date_of_birth')
    address=models.TextField(max_length=100,db_column='address')
    country=models.TextField(max_length=20,db_column='country')
    mobilenumber=models.TextField(max_length=20,db_column='mob_num')
    email=models.TextField(max_length=20,db_column='email')
    password=models.TextField(max_length=15,db_column='password')
    otp=models.CharField(max_length=100,db_column='otp')
    status=models.TextField(max_length=20,default="",db_column='status')

    class Meta:
        db_table='users'
