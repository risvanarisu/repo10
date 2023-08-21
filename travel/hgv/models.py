from django.db import models
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
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
        db_table='guides'

class Hotels(models.Model):
    usercatagory=models.TextField(max_length=50,db_column='user_catagory')
    companyname=models.TextField(max_length=50,db_column='company_name')
    reg_id=models.TextField(max_length=50,db_column='company_reg_id')
    reg_year=models.TextField(max_length=50,db_column='company_reg_year')
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
    reg_year=models.TextField(max_length=50,db_column='company_reg_year')
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





























































class Catagory(models.Model):
    usercatagory=models.TextField(max_length=50,db_column='user_catagory')
    companyname=models.TextField(max_length=50,db_column='company_name')
    regid=models.TextField(max_length=50,db_column='company_reg_id')
    regyear=models.TextField(max_length=50,db_column='company_reg_year')
    account_number=models.TextField(max_length=50,db_column='bank_account_number')
    ifsc_code=models.TextField(max_length=50,db_column='bank_ifsc_code')
    bank_name=models.TextField(max_length=50,db_column='bank_branch_name')
    address=models.TextField(max_length=50,db_column='company_address')
    country=models.TextField(max_length=50,db_column='company_country')
    mobile=models.TextField(max_length=50,db_column='mobile_number')
    email=models.TextField(max_length=50,db_column='company_email')
    user_id=models.IntegerField(null=True,db_column='login_id')
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  

    class Meta:
        db_table='service'

class Add_guide(models.Model):
    first_name=models.TextField(max_length=50,db_column='first_name')
    second_name=models.TextField(max_length=50,db_column='second_name')
    Address=models.TextField(max_length=100,db_column='address')
    country=models.TextField(db_column='country')
    price=models.IntegerField(db_column='price')
    contact=models.TextField(db_column='contact')
    email=models.TextField(max_length=50,db_column='email')
    account_no=models.TextField(max_length=50, null=True,db_column='account no')
    ifsc_code=models.TextField(max_length=50,null=True,db_column='ifsc code')
    bank_name=models.TextField(max_length=50,null=True,db_column='bank name')
    gui_image=models.ImageField(upload_to='images/',db_column='guide_image')

    class Meta:
        db_table='add_guide'   























        


class Add_hotel(models.Model):
    hotel_name=models.TextField(max_length=50,db_column='_hotelname')
    place=models.TextField(max_length=50,db_column='_place')
    price=models.IntegerField(db_column='_price')
    star=models.IntegerField(db_column='_star')
    Address=models.TextField(max_length=100,db_column='_address')
    contact=models.TextField(db_column='_contact')
    rooms=models.TextField( null=True,db_column='rooms_available')
    email=models.TextField(max_length=50,db_column='_email')
    features=models.TextField(max_length=50,db_column='_features')
    account_no=models.TextField(max_length=50, null=True,db_column='_account no')
    ifsc_code=models.TextField(max_length=50,null=True,db_column='_ifsc code')
    bank_name=models.TextField(max_length=50,null=True,db_column='_bank name')
    hotel_image=models.ImageField(upload_to='images/',db_column='_hotelimage')

    class Meta:
         db_table='add_hotel'   

class Add_vehicle(models.Model):
    vehicle_name=models.TextField(max_length=50,db_column='_vehiclename')
    vehicle_id=models.IntegerField(db_column='_vehicleid')
    model=models.TextField(db_column='_model')
    price=models.IntegerField(db_column='_price')
    address=models.TextField(max_length=50,db_column='_address')
    contact=models.TextField(db_column='_contact')
    email=models.TextField(max_length=50,db_column='_email')
    features=models.TextField(max_length=50,db_column='_features') 
    account_no=models.TextField(max_length=50, null=True,db_column='_account no')
    ifsc_code=models.TextField(max_length=50,null=True,db_column='_ifsc code')
    bank_name=models.TextField(max_length=50,null=True,db_column='_bank name')
    vehicle_image=models.ImageField(upload_to='images/',db_column='_vehicleimage')

    class Meta:
          db_table='add_vehicle'   

  

