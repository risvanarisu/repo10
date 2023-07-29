from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings 
from hgv.models import Catagory,Add_hotel,Add_guide,Add_vehicle
#Create your views here.

def gethomepage(request):
    return render(request,"user/homepage.html")

def gethome(request):
    return render(request,"user/home.html")

def getvehicleview(request,v_id):
    vehicle=Add_vehicle.objects.get(id=v_id)
    return render(request,"user/vehicleview.html",{'vehicle_data':vehicle})

def getlogin(request):
    if request.method=="POST":
        _username=request.POST['user_name']
        _password=request.POST['pass_word']
        if '@' in _username:
            user_exist=Users.objects.filter(email=_username,password=_password).exists()
            if user_exist:
                user=Users.objects.get(email=_username,password=_password)
                request.session['user_id']=user.id
                if user.status=='otpverify':
                    otp=randint(1000,9999)
                    send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [user.email],
                
                    )

                    user.otp=otp
                    user.save()
                    return redirect('user:verifyotp')
                return redirect('user:home')
            else:
                return render(request,"user/login",{'message':'invalid user details'})
        elif _username.isdigit():
            service_exist=Catagory.objects.filter(user_id=_username,password=_password).exists()
            
            if service_exist:
                service_data=Catagory.objects.get(user_id=_username,password=_password)
                if service_data.status=='active' and service_data.usercatagory== 'guides':
                    request.session['service_id']=service_data.id
                    return redirect('hgv:guidehome')
                elif service_data.status=='active' and service_data.usercatagory== 'hotels':
                    request.session['service_id']=service_data.id
                    return redirect('hgv:hotelhome')
                elif service_data.status=='active' and service_data.usercatagory== 'vehicles':
                    request.session['service_id']=service_data.id
                    return redirect('hgv:vehiclehome')
                else:
            
                    return render(request,"user/homepage.html",{'message':'account not approved'})
            else:
                return render(request,"user/homepage.html",{'message':'invalid user name or password'})




    return redirect('user:login')

    
    
def getmaster(request):
    return render(request,"user/master.html")

def getsignup(request):
    msg="" 
    if request.method=='POST':
        user_type=request.POST['usertype']
        if user_type=='user':
            u_firstname=request.POST['first_name']
            u_lastname=request.POST['last_name']
            u_gender=request.POST['gen']
            u_dateofbirth=request.POST['dob']
            u_address=request.POST['addre_ss']
            u_country=request.POST['_country']
            u_mobilenumber=request.POST['mobnum']
            u_email=request.POST['emai_l']
            u_password=request.POST['pass_word']
            user_exists=Users.objects.filter(email=u_email).exists()

            if not user_exists:
                otp=randint(1000,9999)
                send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [u_email],

                )


                user_data=Users(first_name=u_firstname,last_name=u_lastname,gender=u_gender,dateofbirth=u_dateofbirth,address=u_address,country=u_country,mobilenumber=u_mobilenumber,email=u_email,password=u_password,otp=str(otp),status='otpverify')
                user_data.save()
                user=Users.objects.get(email=u_email)
                request.session['user_id']=user.id
                
                
                msg='registration successful'
                return redirect('user:verifyotp') 
        if user_type=='hotels' or 'guides' or 'vehicles':
            s_usercatagory=user_type
            s_comp_name=request.POST['name']
            s_company_id=request.POST['id']
            s_company_year=request.POST['year']
            s_account_num=request.POST['account_no']
            s_ifsc_code=request.POST['ifsc_code']
            s_bank_name=request.POST['bank_name']
            s_address=request.POST['addre_ss']
            s_country=request.POST['_country']
            s_mobilenumber=request.POST['mobnum']
            s_email=request.POST['emai_l']
            s_password=request.POST['pass_word']
            s_loginid=randint(1000,9999)
            servicer_exists=Catagory.objects.filter(email=s_email).exists()
            if not servicer_exists:
                servicer_data=Catagory(usercatagory=s_usercatagory,companyname=s_comp_name,regid=s_company_id,regyear=s_company_year,account_number=s_account_num,ifsc_code=s_ifsc_code,bank_name=s_bank_name,address=s_address,country=s_country,mobile=s_mobilenumber,email=s_email,user_id=s_loginid,password=s_password)
                servicer_data.save()
                subject='your login id is '+str(s_loginid)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [s_email],
                                                       
                )
                
                msg='registration successful'
            else:
                msg='email exists'

    return render(request,'user/signup.html',{'message':msg})

def getguides(request):
    guide=Add_guide.objects.all()
    return render(request,"user/guides.html",{'guide_data':guide})

def gethotels(request):
    hotel=Add_hotel.objects.all()
    return render(request,"user/hotels.html",{'hotel_data':hotel})

def gettransportation(request):
    vehicle=Add_vehicle.objects.all()
    return render(request,"user/transportation.html",{'vehicle_data':vehicle})

def getprofile(request):
    u_id=request.session['user_id']
    
    if request.method=='POST':
        user_firstname=request.POST['u_name']
        user_lastname=request.POST['u_lname']
        user_gender=request.POST['u_gen']
        user_email=request.POST['u_email']
        user_contact=request.POST['u_contact']
        user_address=request.POST['u_address']
        user_dateofbirth=request.POST['u_db']
        
       
        
        Users.objects.filter(id=u_id).update(first_name=user_firstname,last_name=user_lastname,gender=user_gender,dateofbirth=user_dateofbirth,address=user_address,mobilenumber=user_contact,email=user_email)
        return redirect('user:profiles')
    else:
        user=Users.objects.get(id=u_id)
        return render(request,"user/profile.html",{'user_data':user})


def getmaster1(request):
    return render(request,"user/master1.html")

def getguideview(request,g_id):
    guide=Add_guide.objects.get(id=g_id)
    return render(request,"user/guideview.html",{'guide_data':guide})

def gethotelviews(request,h_id): 
    hotel=Add_hotel.objects.get(id=h_id)
    return render(request,"user/hotelview.html",{'hotel_data':hotel})



def getbookinghotel(request):
    return render(request,"user/bookinghotel.html")

def getmybookings(request):
    return render(request,"user/mybookings.html")

def getverifyotp(request):
    if request.method=='POST':
        otp=request.POST['o_tp']
        c_id=request.session['user_id']                         
        data=Users.objects.get(id=c_id)
        if otp==data.otp:
            Users.objects.filter(id=c_id).update(status='otp verified')
            return redirect('user:home')
        else:
            return render(request,"user/verifyotp.html",{'message':'invalid otp'})

    return render(request,"user/verifyotp.html")
def changepassword(request):
    
    u_id=request.session['user_id']
    user=Users.objects.get(id=u_id)
    password=Users.objects.get(password)
    if request.method=='POST':
        oldpass=request.POST['old']
        newpass=request.POST['new']
    
    
        if password==oldpass:
            Users.objects.update(password=newpass)
        else:
            return redirect('user:home')
    
    return render(request,"user/home.html",{'message':'password changed successfully'},{'user_data':user})
def logout(request):
    request.session.delete()
    return redirect('user:homepage')
