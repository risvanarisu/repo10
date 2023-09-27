from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings 
from hgv.models import Add_hotel,Add_vehicle,Guides,Hotels,Vehicles,Guide_book,Hotel_book,Vehicle_book
#Create your views here.

def gethomepage(request):
        
    return render(request,"user/homepage.html")

def gethome(request):
    
        
    return render(request,"user/home.html")

def getgsearch(request):

        
    return redirect('user:guides')

def getvehicleview(request,v_id):
    vehicle=Add_vehicle.objects.filter(vehicle_id=v_id)
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
    return redirect('user:login')

    
    
def getmaster(request):
    
        
    return render(request,"user/master.html")

def getsignup(request):
    msg="" 
    if request.method=='POST':
        # user_type=request.POST['usertype']
        # if user_type=='user':
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

    return render(request,'user/signup.html',{'message':msg})
                  

def getguides(request):
    if 'user_id' in request.session :
        guide=Guides.objects.all()
    return render(request,"user/guides.html",{'guide_data':guide})
                   
    
def gethotels(request):
    if 'user_id' in request.session :
        hotel=Hotels.objects.all()
    return render(request,"user/hotels.html",{'hotel_data':hotel})
                   

def gettransportation(request):
    if 'user_id' in request.session :
        vehicle=Vehicles.objects.all()
    return render(request,"user/transportation.html",{'vehicle_data':vehicle})

def getprofile(request):
    if 'user_id' in request.session :
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
    guide=Guides.objects.get(id=g_id)    
    return render(request,"user/guideview.html",{'guide_data':guide})

def gethotelviews(request,h_id):
    hotel=Add_hotel.objects.filter(hotel_id=h_id)
    return render(request,"user/hotelview.html",{'hotel_data':hotel})


def getbookinghotel(request,h_id):
    u_id=request.session['user_id']
    if request.method=='POST':
        start_date=request.POST['firstdate']
        end_date=request.POST['lastdate']
        total_members=request.POST['members']
        rooms=request.POST['total']
        days=request.POST['day_s']
        # userid=Users.objects.get(id=u_id)
        hotel=Hotels.objects.get(id=h_id)
        booking=Hotel_book(check_in=start_date,check_out=end_date,members=total_members,total_rooms=rooms,total_days=days,user_id=u_id,hotel_id=hotel.id)
        booking.save()
           
    return render(request,"user/bookinghotel.html")

def getbookvehicle(request,v_id):
    u_id=request.session['user_id']
    if request.method=='POST':
        startdate=request.POST['first']
        enddate=request.POST['last']
        totaldays=request.POST['total']
        userid=Users.objects.get(id=u_id)
        vehicle=Vehicles.objects.get(id=v_id)
        booking=Vehicle_book(start_date=startdate,end_date=enddate,total_days=totaldays,user_id=userid,vehicle_id=vehicle)
        booking.save()
    return render(request,"user/bookvehicle.html")


def getbookguide(request,g_id):
    u_id=request.session['user_id']
    if request.method=='POST':
        first_date=request.POST['firstdate']
        last_date=request.POST['lastdate']
        days=request.POST['day_s']
        userid=Users.objects.get(id=u_id)
        guide=Guides.objects.get(id=g_id)
        booking=Guide_book(start_date=first_date,end_date=last_date,total_days=days,user_id=userid,guide_id=guide,status='booking pending')
        booking.save()
           
            
    return render(request,"user/bookguide.html")

def getmybookings(request):
    # if 'user_id' in request.session :
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

def getemailverify(request):
    if request.method=='POST':
        new_otp=request.POST['otp_']
        u_id=request.session['user_id']                         
        data=Users.objects.get(id=u_id)
        if new_otp==data.otp:
            return redirect('user:resetpassword')
        else:
            
        

            return render(request,"user/emailverify.html",{'message':'invalid otp'})
    return render(request,"user/emailverify.html")

def changepassword(request):
    
    u_id=request.session['user_id']
    user=Users.objects.get(id=u_id)
    oldpassword=user.password
    if request.method=='POST':
        oldpass=request.POST['old']
        newpass=request.POST['new']
    
    
        if oldpassword==oldpass:
            Users.objects.filter(id=u_id).update(password=newpass)
        else:
            return redirect('user:home')
    
    return render(request,"user/home.html",{'user_data':user})

def getlogout(request):
    del request.session['user_id']
    return redirect('user:homepage')

def getforget(request):
    if request.method=="POST":
        user_name=request.POST['user']
        if '@' in user_name:  
            user_exist=Users.objects.filter(email=user_name).exists()
            if user_exist:
                user=Users.objects.get(email=user_name)
                request.session['user_id']=user.id
                
                otp_n=randint(1000,9999)
                send_mail(
                'please verify your otp',
                    str(otp_n),
                    settings.EMAIL_HOST_USER,
                    [user_name],
            
                )
                u_id=request.session['user_id']
                Users.objects.filter(id=u_id).update(otp=otp_n)

        
                return redirect('user:email_verify')
            else:
                return render(request,"user/forgetpass.html",{'message':'email does not exist'})
    return render(request,"user/forgetpass.html")

def getresetpassword(request):
    
    if request.method=="POST":
        reset_password=request.POST['pass_word']
        u_id=request.session['user_id']
        Users.objects.filter(id=u_id).update(password=reset_password)
        return render(request,"user/resetpassword.html",{'message':'password changed succefully'})

    return render(request,"user/resetpassword.html")
