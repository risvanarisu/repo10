from django.db import models
from user.models import Users
from datetime import datetime

# Create your models here.

class Guides(models.Model):
    usercatagory=models.TextField(max_length=50,db_column='user_catagory')
    first_name=models.TextField(max_length=30,db_column='f_name')
    last_name=models.TextField(max_length=30,db_column='l_name')
    gender=models.CharField(max_length=6,db_column='gender')
    dateofbirth=models.DateField(db_column='date_of_birth')
    account_number=models.TextField(max_length=50,db_column='bank_account_number')
    ifsc_code=models.TextField(max_length=50,db_column='bank_ifsc_code')
    bank_name=models.TextField(max_length=50,db_column='bank_branch_name')
    address=models.TextField(max_length=50,db_column='company_address')
    country=models.TextField(max_length=50,db_column='company_country')
    mobile=models.TextField(max_length=50,db_column='mobile_number')
    email=models.TextField(max_length=50,db_column='company_email')
    user_id=models.IntegerField(null=True,db_column='login_id')
    password=models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
        db_table='guides'

class Hotels(models.Model):
    usercatagory=models.TextField(max_length=50,db_column='user_catagory')
    companyname=models.TextField(max_length=50,db_column='company_name')
    reg_id=models.TextField(max_length=50,db_column='company_reg_id')
    reg_year=models.DateField(db_column='company_reg_year')
    account_number=models.TextField(max_length=50,db_column='bank_account_number')
    ifsc_code=models.TextField(max_length=50,db_column='bank_ifsc_code')
    bank_name=models.TextField(max_length=50,db_column='bank_branch_name')
    address=models.TextField(max_length=50,db_column='address')
    country=models.TextField(max_length=50,db_column='country')
    mobile=models.TextField(max_length=50,db_column='mobile')
    email=models.TextField(max_length=50,db_column='email')
    user_id=models.IntegerField(null=True,db_column='login_id')
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
        db_table='hotels'


class Vehicles(models.Model):
    usercatagory=models.TextField(max_length=50,db_column='user_catagory')
    companyname=models.TextField(max_length=50,db_column='company_name')
    reg_id=models.TextField(max_length=50,db_column='company_reg_id')
    reg_year=models.DateField(db_column='company_reg_year')
    account_number=models.TextField(max_length=50,db_column='bank_account_number')
    ifsc_code=models.TextField(max_length=50,db_column='bank_ifsc_code')
    bank_name=models.TextField(max_length=50,db_column='bank_branch_name')
    address=models.TextField(max_length=50,db_column='address')
    country=models.TextField(max_length=50,db_column='country')
    mobile=models.TextField(max_length=50,db_column='mobile')
    email=models.TextField(max_length=50,db_column='email')
    user_id=models.IntegerField(null=True,db_column='login_id')
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
        db_table='vehicles'


class Add_hotel(models.Model):
    hotel_id=models.ForeignKey(Hotels,on_delete=models.CASCADE,null=True,db_column='hotel_id')
    room_type=models.TextField(null=True,max_length=20,db_column='rooms_name')
    price=models.IntegerField(db_column='_price')
    star=models.IntegerField(db_column='_star')
    rooms=models.TextField( null=True,db_column='rooms_available')
    features=models.TextField(max_length=50,db_column='_features')
    hotel_image=models.ImageField(upload_to='images/',db_column='_hotelimage')

    class Meta:
         db_table='add_hotel'  



class Guide_book(models.Model):
    guide_id=models.ForeignKey(Guides,on_delete=models.CASCADE,null=True,db_column='guide_id')
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,db_column='user_id')
    start_date=models.DateField(db_column='start_date')
    end_date=models.DateField(db_column='end_date')
    total_days=models.IntegerField(db_column='total_days')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  
    status=models.TextField(max_length=20,default="",db_column='status')

    class Meta:
          db_table='guide_bookings'   




class Vehicle_book(models.Model):
    vehicle_id=models.ForeignKey(Vehicles,on_delete=models.CASCADE,null=True,db_column='hotel_id')
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,db_column='user_id')
    start_date=models.DateField(db_column='start_date')
    end_date=models.DateField(db_column='end_date')
    total_days=models.IntegerField(db_column='total_days')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
          db_table='vehicle_bookings'   


class Hotel_book(models.Model):
    hotel_id=models.ForeignKey(Hotels,on_delete=models.CASCADE,null=True,db_column='hotel_id')
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,db_column='user_id')
    check_in=models.DateField(db_column='check_in_date')
    check_out=models.DateField(db_column='check_out_date')
    members=models.TextField(db_column='members_list')
    total_rooms=models.IntegerField(db_column='total_rooms')
    total_days=models.IntegerField(db_column='total_days')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
          db_table='hotelbookings'   


class Add_vehicle(models.Model):
    
    vehicle_id=models.ForeignKey(Vehicles,on_delete=models.CASCADE,null=True,db_column='vehicles_id')
    model=models.TextField(db_column='_model')
    price=models.IntegerField(db_column='_price')
    features=models.TextField(max_length=50,db_column='_features') 
    vehicle_image=models.ImageField(upload_to='images/',db_column='_vehicleimage')

    class Meta:
          db_table='add_vehicle'   

  